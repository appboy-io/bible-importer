ERROR_CONSTANTS = {
    'GITHUB_NOT_FOUND': "Github is not installed on this system",
    'GITHUB_REPO_NOT_FOUND': "Github repo could not be downloaded",
    'GITHUB_DIR_DELETE_ERR': "Can't delete bible directory"
}

class SystemCheckException(Exception):
    """Raise this exception when a system check fails"""
    def __init__(self, message):
        super().__init__(message)
    