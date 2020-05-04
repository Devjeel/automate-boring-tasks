import os
from os.path import join, dirname
from dotenv import load_dotenv
from github import Github

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# using an access token
g = Github(os.environ.get("GITHUB_API"))

def get_all_repos:
    for repo in g.get_user().get_repos():
        print("========== Your GitHub Repos ============")
        print(repo.name)
