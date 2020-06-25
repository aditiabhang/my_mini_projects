
from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    # Note 1 code
    html.render()

match2 = html.find('#footer', first = True)
print('Dynamic data: ', match2.html)
print("")

print(html.text) #printing the text
print("------------------------------------------")

match = html.find('title') 
#print(match)   #printing elements that are found with title 
print(match[0].text) #printing only the text of the first element

#instead of using the index, we can tell the find method to print only the first element as below:
match1 = html.find('title', first = True)
print(match1.text)

print("------------------------------------------")
article = html.find('div.article', first = True)
print(article.text)

#headline and summary
headline = article.find('h2', first = True).text
summary = article.find('p', first = True).text

print("Headline only: ", headline)
print("Summary only: ", summary)

'''
Note1 - Difference between HTML-request and Beautiful soup:
HTML requests enable us to render the dynamically generated data by javascript.
We need to render the page in order to get the dynamic data using;
html.render() - first time run this it might need to download some things from premium, 
so dont worry if this shows some downloading.

'''