#
#    A whole new file explorer for macOS. Finder, but better.
#    Copyright (C) 2023  Dishant B. (@dishb) <code.dishb@gmail.com> and
#    contributors.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import os
from shutil import copyfileobj, rmtree

import requests


def download_dir(repo: str, dir_path: str, dest_path: str) -> None:
    """
    Downloads any folder from a Github repository.
    """

    # Extract the repository owner and name from the URL
    url_parts = repo.split("/")
    owner = url_parts[0]
    repo_name = url_parts[1]
    repo_url = f"https://github.com/{owner}/{repo_name}"

    # API endpoint for the repository contents
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{dir_path}"

    # Send a GET request to the API endpoint
    response = requests.get(api_url, timeout = 5)
    if response.status_code == 200:
        contents = response.json()
        if os.path.exists(dest_path):
            rmtree(dest_path)

        os.makedirs(dest_path)

        for item in contents:
            if item["type"] == "file":
                # Download files
                file_url = item["download_url"]
                file_name = os.path.basename(file_url)
                file_path = os.path.join(dest_path, file_name)
                response = requests.get(file_url, stream = True, timeout = 5)

                with open(file_path, "wb") as file:
                    response.raw.decode_content = True
                    copyfileobj(response.raw, file)
                    file.close()

            elif item["type"] == "dir":
                # Recursively download subdirectories
                subdir_path = os.path.join(dest_path, item["name"])
                download_dir(repo_url, item["path"], subdir_path)

        print("\nSuccessfully retrieved directory contents.")
        print(f"Response: {response.status_code}")
        print(f"Repository: {owner}/{repo_name}")
        print(f"Folder requested: {dir_path}")
        print(f"Destination: {dest_path}")

    else:
        print("\nFailed to retrieve directory contents.")
        print(f"Response: {response.status_code}")
        print(f"Repository: {owner}/{repo_name}")
        print(f"Folder requested: {dir_path}")
        print(f"Destination: {dest_path}")

download_dir("TomSchimansky/CustomTkinter",
                "customtkinter",
                "../customtkinter/"
                )
