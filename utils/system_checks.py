from utils.error_constants import ERROR_CONSTANTS, SystemCheckException
from utils.constants import APP_CONSTANT
import subprocess

class SystemChecks():
    def checkGit():
        git_exist = subprocess.run(["git", "--version"])
        if git_exist.returncode != 0:
            raise SystemCheckException(ERROR_CONSTANTS['GITHUB_NOT_FOUND'])

    def repoCheck():
        git_exist = subprocess.run(["git", "ls-remote", APP_CONSTANT['REPO']])
        if git_exist.returncode != 0:
            raise SystemCheckException(ERROR_CONSTANTS['GITHUB_REPO_NOT_FOUND'])

def full_system_check():
    [SystemChecks.checkGit(), SystemChecks.repoCheck()]