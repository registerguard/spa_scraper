import pickle
from pprint import pprint

from bs4 import BeautifulSoup

html = pickle.load( open( 'usatf.p', 'rb'))

soup = BeautifulSoup(html)

# Get the event title bits
event_title = soup.find(id='appBarTitle')
print [t for t in event_title.stripped_strings]

# qualifying notes (Note: May be None)
q_note = soup.find('div', class_='qNote')
print [n for n in q_note.stripped_strings]

# page out list
total_out = []

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

pprint(total_out)
