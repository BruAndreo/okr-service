from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer
from okr.utils.jwt import JWT

class AuthenticationMiddleware(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(AuthenticationMiddleware, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials = await super(AuthenticationMiddleware, self).__call__(request)
        if not credentials:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authorization code")

        if not self._is_bearer(credentials.scheme):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Authentication Scheme")
        
        try:
            print(credentials.credentials)
            decoded_token = JWT.decode(credentials.credentials)
            print(decoded_token)
        except Exception as err:
            print(err)
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=err)


    def _is_bearer(self, scheme):
        return scheme == "Bearer"