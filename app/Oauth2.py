from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas,database, models
from fastapi import status, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


#this give the token url when user tries to login with its username and password
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
#SECRET_KEY
#Algorithm
#expiration time of the token

#openssl rand -hex 32

SECRET_KEY = "1b0b01deb22e015c2e69937713016261699ae7c5fd9fe63ae5deaf9f59ea6e97"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_TIME = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm= ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])

        id1: str = payload.get("user_id")

        if id1 is None:
            raise credentials_exception
        
        token_data =schemas.TokenData(id=str(id1))
    except JWTError as e:
        print(e)
        raise credentials_exception
    
    
    return token_data
    

def get_current_user(token: str = Depends(oauth2_scheme),db : Session= Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials",
                                          headers={"WWW-Authenticate" : "Bearer"})
    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user 

