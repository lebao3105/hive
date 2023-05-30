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

from shutil import copyfileobj
import os

import requests

def download_folder(repo_url: str, folder_path: str, destination_path: str) -> None:
    """
    Downloads any folder from a Github repository.
    """

    # Extract the repository owner and name from the URL
    url_parts = repo_url.split("/")
    owner = url_parts[-2]
    repo_name = url_parts[-1].split(".")[0]

    # API endpoint for the repository contents
    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/contents/{folder_path}"

    # Send a GET request to the API endpoint
    response = requests.get(api_url, timeout = 5)
    if response.status_code == 200:
        contents = response.json()
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        for item in contents:
            if item["type"] == "file":
                # Download files
                file_url = item["download_url"]
                file_name = os.path.basename(file_url)
                file_path = os.path.join(destination_path, file_name)
                response = requests.get(file_url, stream = True, timeout = 5)
                with open(file_path, "wb") as file:
                    response.raw.decode_content = True
                    copyfileobj(response.raw, file)
                del response

            elif item["type"] == "dir":
                # Recursively download subdirectories
                subdir_path = os.path.join(destination_path, item["name"])
                download_folder(repo_url, item["path"], subdir_path)
    else:
        print(f"Failed to retrieve folder contents. Status code: {response.status_code}")

download_folder("https://github.com/TomSchimansky/CustomTkinter",
                       "customtkinter",
                       "../customtkinter/"
                       )
