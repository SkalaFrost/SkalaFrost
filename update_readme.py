import requests
import os

GITHUB_USERNAME = "SkalaFrost"
README_PATH = "README.md"

def fetch_repos():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url)
    return response.json()

def update_readme(repos):
    table_header = """
<table>
  <thead align="center">
    <tr border: none;>
      <td><b>&#x1F916; Bot</b></td>
      <td><b>&#x2B50; Stars</b></td>
      <td><b>&#x1F4DA; Forks</b></td>
      <td><b>&#x1F6CE; Issues</b></td>
      <td><b>&#x1F4EC; Pull requests</b></td>
    </tr>
  </thead>
  <tbody>
"""
    
    table_rows = ""
    for repo in repos:
        repo_name = repo["name"]
        stars = repo["stargazers_count"]
        forks = repo["forks_count"]
        issues = repo["open_issues_count"]
        pulls = repo["open_issues_count"]  

        table_rows += f"<tr><td><a href=\"{repo['html_url']}\"><b>{repo_name}</b></a></td><td><img alt=\"Stars\" src=\"https://img.shields.io/github/stars/{GITHUB_USERNAME}/{repo_name}?style=flat-square&labelColor=343b41\"/></td><td><img alt=\"Forks\" src=\"https://img.shields.io/github/forks/{GITHUB_USERNAME}/{repo_name}?style=flat-square&labelColor=343b41\"/></td><td><img alt=\"Issues\" src=\"https://img.shields.io/github/issues/{GITHUB_USERNAME}/{repo_name}?style=flat-square&labelColor=343b41\"/></td><td><img alt=\"Pull Requests\" src=\"https://img.shields.io/github/issues-pr/{GITHUB_USERNAME}/{repo_name}?style=flat-square&labelColor=343b41\"/></td></tr>\n"

    table_footer = """
  </tbody>
</table>
"""
    
    table_content = table_header + table_rows + table_footer

    with open(README_PATH, "r", encoding="utf8") as readme:
        content = readme.read()


    new_content = content.replace(
        content[content.find("<table"):content.find("</table>") + 8],
        table_content
    )

    with open(README_PATH, "w", encoding="utf8") as readme:
        readme.write(new_content)

if __name__ == "__main__":
    repos = fetch_repos()
    update_readme(repos)
