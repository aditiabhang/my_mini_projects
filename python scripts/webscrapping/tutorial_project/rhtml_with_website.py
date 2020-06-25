import csv  # to write the output into a csv file
from requests_html import HTML, HTMLSession

csv_file = open('cms_scaper.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video'])

session = HTMLSession()
response_obj = session.get('https://coreyms.com/')
#print(response_obj.html)

articles = response_obj.html.find('article')
for article in articles:
# print(article.html) # prints out html of the first article
# adding the for loop, because we want all the articles now..and removing first = True
    headline = article.find('.entry-title-link', first = True).text
    print('\nHeadline: ', headline)
    print("")

    summary = article.find('.entry-content p', first = True).text
    print('Summary: ', summary)
    print("")

    #video_src = article.find('iframe', first = True)
    #print(video_src.attrs['src'])       #attrs = attributes, just like dictionary ,
                                         # and the 'src' is a key
    #print(video_src)

    # try except block to check for errors/missing attributes
    try:
        video_src = article.find('iframe', first = True).attrs['src']
        # Now we get the ID present in the url by using split method
        # The ID is present at the 4th index, hence use [4]
        video_id = video_src.split('/')[4]
        video_id = video_id.split('?')[0]
        #print('YOUTUBE Video ID: ',video_id)
        yt_link = f'https://www.youtube.com/watch?v={video_id}'
    except Exception as e:
        t_link = None
    
    print('YOUTUBE link: ', yt_link)
    print("")

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()



'''
Now we loop over all of the articles and get that information for all of them.
We add the for loop. 
Now sometimes, there can be a case when the find method cannot find a attribute in the list, in such case we try except block.
This is check for errors, if found it will just skip that part.
'''

