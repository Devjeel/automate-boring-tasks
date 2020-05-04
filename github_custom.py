from github import Github

# using an access token
g = Github("<<token>>")

def get_all_repos:
    for repo in g.get_user().get_repos():
        print("========== Your GitHub Repos ============")
        print(repo.name)