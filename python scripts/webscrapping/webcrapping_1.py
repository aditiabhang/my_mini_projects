
from requests_html import HTML, HTMLSession

session = HTMLSession()
response_obj = session.get('https://cs.txstate.edu/accounts/profiles/v_m137/')

# Extracting the name of the professor
prof_name = response_obj.html.find('h1.heading-title.pull-left', first = True)
print('\nName: ', prof_name.text)

# # Extracting Education of the professor
# education = response_obj.html.find('div.panel-body p', first = True)
# print('Education: ', education.text)

# Extracting the Research interest of the professor
research_interest = response_obj.html.find('div.panel-body p', first = True)
print('\nResearch interest: ', research_interest.text)

# Extracting webpage url
webpage_link = response_obj.html.find('h3 a', first = True)
#print('Webpage: ', webpage_link.html)       # gives out the html of the mentioned find
print('\nWebpage: ', webpage_link.attrs['href'])


