from pydantic import BaseModel

#회원가입 DTO
class Register_User(BaseModel):
  user_id:str
  password:str
  user_name:str
  nickname:str
  email:str
  user_number:str
  user_age:int


#로그인 DTO
class Login_User(BaseModel):
  user_id:str
  password:str


#회원가입 반환 DTO
class Response_Register(BaseModel):
  status:int
  message:str


#로그인 반환 DTO
class Response_Login(BaseModel):
  status:int
  message:str
  data:str