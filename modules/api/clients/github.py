import requests
from dotenv import load_dotenv
import os

class Github:

    # Fetch user details by username
    def get_user(self,username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body
    
    # Search repositories by name with pagination
    def get_repositories(self,reponame,per_page):
        r =requests.get(f"https://api.github.com/search/repositories?q={reponame}&per_page={per_page}")
        body = r.json()

        return body
    
     # Search repositories with raw response
    def get_repositories_no_name(self,reponame,per_page):
        r =requests.get(f"https://api.github.com/search/repositories?q={reponame}&per_page={per_page}")
        
        return r
    
    # Create a new repository
    def create_repo(self, name_of_repo):
        load_dotenv()
        github_token = os.getenv("GITHUB_TOKEN")
        
        github_api_url = "https://api.github.com"
        #Autorization
        headers = {
            "Authorization": f"token {github_token}",
            
        }

        #Data for create repo
        repo_data = {
            "name": f"{name_of_repo}",
            "description": "This is a test repository created via API",
            "private": False  # False for pablick, True for privat
        }

        
        r = requests.post(f"{github_api_url}/user/repos", json=repo_data, headers=headers)
        
        return r
    
    # Delete a repository
    def delete_repo(self,repo_name):
        load_dotenv()
        github_token = os.getenv("GITHUB_TOKEN")
        owner = "api-test-akaunt"
        repo_name = repo_name
        
        url = f"https://api.github.com/repos/{owner}/{repo_name}"

        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        r = requests.delete(url, headers=headers)
        return r
    
    # Fetch all GitHub emojis
    def get_emojis(self):
        url = "https://api.github.com/emojis"
        r = requests.get(url)
        return r
     
    # Update repository details
    def updare_repo(self, owner , repo , description):
        load_dotenv()
        github_token = os.getenv("GITHUB_TOKEN")
        new_description = {"description": f"{description}"}
        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        url = f"https://api.github.com/repos/{owner}/{repo}"
        r = requests.patch(url, json=new_description, headers=headers)
        return r