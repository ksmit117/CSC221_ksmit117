import requests
import plotly.express as px

#Make a API call and check the response
#shows the most starred projects using Ruby

url = 'https://api.github.com/search/repositories?q=language:Ruby&sort=stars'
url += "?q=language:python+sort:stars+stars:>10000"


headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# process overall results
response_dict = r.json()
print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], [],
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    #turn repo names into active links
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
print(f"Repositories returned: {len(repo_dicts)}")


# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)


print("\nSelected information about each repository:")
print("\nSelected information about first repository:")
for repo_dict in repo_dicts:

    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}") 
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

#build hover texts
owner = repo_dict['owner']['login']
description = repo_dict['description']
hover_text = f"{owner}<br />{description}"
hover_texts.append(hover_text)

 # Make visualization
title = "Most-Starred Ruby Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()
