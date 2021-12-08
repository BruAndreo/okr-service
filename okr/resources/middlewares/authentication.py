from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer

class AuthenticationMiddleware(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(AuthenticationMiddleware, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials = await super(AuthenticationMiddleware, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid Authentication Scheme")
            print(credentials.credentials)
            # TODO: Created JWT decode validation and raise exceptions when invalid
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")