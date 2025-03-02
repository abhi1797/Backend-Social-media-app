from fastapi import Response, status, HTTPException,  Depends, APIRouter
from .. import models, schemas, Oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional
from sqlalchemy import func


router = APIRouter(
    prefix="/posts",
    tags= ['Posts']
)

# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_id : int =Depends(Oauth2.get_current_user),
               limit: int = 10,skip: int = 0, search: Optional[str]= ""):
    # cursor.execute("""SELECT * FROM posts """)
    # posts= cursor.fetchall()
    
    #posts=db.query(models.Post).filter(models.Post.title.contains(search)).offset(skip).limit(limit).all()
    posts = db.query(models.Post,
            func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id,
            isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).offset(skip).limit(limit).all()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def Create_Post(post : schemas.PostCreate,db: Session = Depends(get_db), current_user : int =Depends(Oauth2.get_current_user)):

    new_post = models.Post(owner_id=current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id: int,db: Session = Depends(get_db), current_user : int =Depends(Oauth2.get_current_user)):   #if response : Response
    
    # cursor.execute("""SELECT * from posts where id = %s """,(str(id),))
    # single_post = cursor.fetchone()
    # print(single_post)
    # single_post = db.query(models.Post).filter(models.Post.id == id).first()
    single_post =  db.query(models.Post,
            func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id,
            isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not single_post:
        
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id={id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id={id} not found")   
    return single_post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user : int =Depends(Oauth2.get_current_user)):
    # cursor.execute(""" DELETE FROM posts where id = %s RETURNING * """, (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id= {id} does not exists")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action" )
    


    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
  
@router.put("/{id}", response_model=schemas.Post)
def update_post(id : int, updated_post :schemas.PostCreate, db: Session = Depends(get_db), current_user : int =Depends(Oauth2.get_current_user)):
    # cursor.execute(""" UPDATE posts SET title= %s, Content= %s, published=%s WHERE id = %s RETURNING *""",
    #                (post.title,post.content,post.published,str(id),))
    # updated_post= cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if  post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id= {id} does not exists")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action" )
    
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()

    return post_query.first()


"""
from fastapi.params import Body
@router.post("/createposts")
def Create_Post(payload: dict = Body(...)):
    print(payload)
    return {"new post" : f"title : {payload['title']} content : {payload['content']}"}
"""