import requests
import os

GITHUB_USERNAME = "SkalaFrost"
README_PATH = "README2.md"

def fetch_repos():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url)
    return response.json()

def update_readme(repos):
    table_header = """
<table>
  <thead align="center">
    <tr>
      <td><b>🤖 Bot</b></td>
      <td><b>⭐ Stars</b></td>
      <td><b>📚 Forks</b></td>
      <td><b>🛎 Issues</b></td>
      <td><b>📬 Pull requests</b></td>
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
        pulls = repo["open_issues_count"]  # Pull requests count needs a separate API call

        table_rows += f"""
        <tr>
          <td><a href="{repo['html_url']}"><b>{repo_name}</b></a></td>
          <td>{stars}</td>
          <td>{forks}</td>
          <td>{issues}</td>
          <td>{pulls}</td>
        </tr>
        """
    
    table_footer = """
  </tbody>
</table>
"""
    
    table_content = table_header + table_rows + table_footer

    with open(README_PATH, "r") as readme:
        content = readme.read()

    # Replace the existing table with the new one
    new_content = content.replace(
        content[content.find("<table"):content.find("</table>") + 8],
        table_content
    )

    with open(README_PATH, "w") as readme:
        readme.write(new_content)

if __name__ == "__main__":
    repos = fetch_repos()
    update_readme(repos)
