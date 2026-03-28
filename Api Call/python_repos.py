"""Make an Api call and check the response."""
import plotly.express as px
import requests

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Convert the response object to a dictionary.
res_dict = r.json()

# Process overall results:
print(f'Total repositories: {res_dict['total_count']}')
print(f'Complete results: {not res_dict['incomplete_results']}')

# Process repository results.
repo = res_dict['items']
repo_links = [f"<a href='{i['html_url']}'>{i['name']}</a>" for i in repo]
stars = [i['stargazers_count'] for i in repo]
hover_text = [f"{i['owner']['login']}<br />{i['description']}" for i in repo]


# Visualizations
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}

fig = px.bar(x=repo_links, y=stars, labels=labels, title=title,
             hover_name=hover_text)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20, )

fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
