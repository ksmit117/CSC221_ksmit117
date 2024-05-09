from operator import itemgetter
import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")
submission_ids = r.json()

# Process information about each submission.
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
   
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants']}
    submission_dicts.append(submission_dict)


submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)


for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}") 
    print(f"Discussion link: {submission_dict['hn_link']}") 
    print(f"Comments: {submission_dict['comments']}")
    


# Plot the data.
title = "Active Discussions on Hacker News"
fig = px.bar(x=titles, y=num_comments, text=disc_links, title=title, labels={'x': 'Title', 'y': 'Number of Comments'})
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()
