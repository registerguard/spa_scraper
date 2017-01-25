# https://www.youtube.com/watch?v=ufBjNfefIN0
# import pickle
from pprint import pprint
import time

from bs4 import BeautifulSoup
from selenium import webdriver

SITE_ADDR = 'http://trialsresults.usatf.org/'

DAYS = {
    'June 30': ('//*[@id="leftNav"]/div[2]/div[1]/div[1]/b', 2),
    'July 1':  ('//*[@id="leftNav"]/div[2]/div[2]/div[1]/b', 10),
    'July 2':  ('//*[@id="leftNav"]/div[2]/div[3]/div[1]/b', 25),
    'July 3':  ('//*[@id="leftNav"]/div[2]/div[4]/div[1]/b', 16),
    'July 4':  ('//*[@id="leftNav"]/div[2]/div[5]/div[1]/b', 8),
    'July 6':  ('//*[@id="leftNav"]/div[2]/div[6]/div[1]/b', 2),
    'July 7':  ('//*[@id="leftNav"]/div[2]/div[7]/div[1]/b', 14),
    'July 8':  ('//*[@id="leftNav"]/div[2]/div[8]/div[1]/b', 13),
    'July 9':  ('//*[@id="leftNav"]/div[2]/div[9]/div[1]/b', 11),
    'July 10': ('//*[@id="leftNav"]/div[2]/div[10]/div[1]/b', 12),
}

class ScrapingBrowser(webdriver.Firefox):
    def __init__(self, addr, *args, **kwargs):
        super(ScrapingBrowser, self).__init__(*args, **kwargs)
        self.implicitly_wait(6)
        self.get(addr)

    def click_tf_event(self, location):
        # the men's 5000 final button in lh navigation
        # self.find_element_by_xpath('//*[@id="sked"]/table/tbody/tr[10]').click()
        self.find_element_by_xpath(location).click()

if __name__ == '__main__':
    browser = ScrapingBrowser(SITE_ADDR)
    for event_date in DAYS.keys():
        print '\nStarting {0} ... \n'.format(event_date)
        browser.click_tf_event(DAYS[event_date][0])
        time.sleep(.8)
        for tr_count in range(1, (DAYS[event_date][1] + 1)):
            browser.click_tf_event( '//*[@id="sked"]/table/tbody/tr[{0}]/td[2]'.format(tr_count) )
            time.sleep(.6)

            soup = BeautifulSoup(browser.page_source)

            # Get the event title bits
            event_title = soup.find(id='appBarTitle')
            event_title_list = [t for t in event_title.stripped_strings]

            # qualifying notes (Note: May be None)
            q_note = soup.find('div', class_='qNote')
            if q_note:
                q_note_list = [n for n in q_note.stripped_strings]
            else:
                q_note_list = None

            total_out = []
            total_out.append(event_title_list)
            total_out.append(q_note_list)

            for row in soup.find_all('tr'):
                # print '----------'
                row_out = []
                for good_cell in row.find_all('td', class_='bold'):
                    # Not the bold item with the affiliation
                    if good_cell.find('div', class_='affiliation') == None:
                        row_out.append(good_cell.text.strip())
                    else:
                        # <td class="athlete bold" colspan="1" is="null">
                        #     <span is="null">Rochelle Kanuho</span>
                        #     <div class="affiliation" is="null">HOKA ONE ONE NAZ Elite</div>
                        # </td>

                        row_out.extend( [u'{0}'.format(good_cell.span.text.strip()), u'{0}'.format(good_cell.div.text.strip())] )
                    # print row_out
                if row_out:
                    total_out.append(row_out)

            pprint (total_out)
    browser.close()
    browser.quit()
