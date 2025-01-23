import requests
from dotenv import load_dotenv
import os
import sys


load_dotenv()

class Github:

    def __init__(self):
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token: 
            raise RuntimeError("No token provided. Exiting...")
        
        print("token insid")
        #Autorization
        self.headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
    
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
        github_api_url = "https://api.github.com"

        #Data for create repo
        repo_data = {
            "name": f"{name_of_repo}",
            "description": "This is a test repository created via API",
            "private": False  # False for pablick, True for privat
        }
      
        r = requests.post(f"{github_api_url}/user/repos", json=repo_data, headers = self.headers)
        
        return r
    
    # Delete a repository
    def delete_repo(self,repo_name):
        
        owner = "api-test-akaunt"
        repo_name = repo_name
        
        url = f"https://api.github.com/repos/{owner}/{repo_name}"

        r = requests.delete(url, headers= self.headers)
        return r
    
    # Fetch all GitHub emojis
    def get_emojis(self):
        url = "https://api.github.com/emojis"
        r = requests.get(url)
        return r
     
    # Update repository details
    def updare_repo(self, owner , repo , description):
        
        new_description = {"description": f"{description}"}

        url = f"https://api.github.com/repos/{owner}/{repo}"
        r = requests.patch(url, json=new_description, headers= self.headers)
        return r