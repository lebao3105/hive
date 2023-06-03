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

import requests

def new_commit(repo: str) -> str | None:
    """
    Checks if a repo has recieved a commit.
    """
    url = f"https://api.github.com/repos/{repo}/commits"

    response = requests.get(url, timeout = 5)
    if response.status_code == 200:
        commits = response.json()
        if commits: # pylint: disable=no-else-return
            latest_commit_sha = commits[0]["sha"]
            return latest_commit_sha
        else:
            return None

    print("\nFailed to retrieve commit data.")
    print(f"Repository: {repo}")
    print(f"Response: {response.status_code}")
    return None

ctk_commit = new_commit("TomSchimansky/CustomTkinter")

if ctk_commit:
    print(f"A new commit has been pushed: {ctk_commit}")
else:
    print("No new commits have been pushed.")
