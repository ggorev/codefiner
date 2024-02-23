from fastapi import HTTPException, status


class BaseException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class InvalidGitlabLinkException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Invalid Gitlab Link."
