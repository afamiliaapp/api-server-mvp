from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional


# -------------------------
# SIGN IN
# -------------------------

class SignInRequest(BaseModel):
    email: EmailStr
    password: Optional[str] = None
    google_token: Optional[str] = None


# -------------------------
# SIGN UP STEP 1
# -------------------------

class SignUpRequest(BaseModel):

    surname: str
    firstname: str
    othername: Optional[str]

    email: EmailStr

    country_code: str
    phone_number: str

    preferred_language: str

    date_of_birth: date

    password: Optional[str] = None
    google_token: Optional[str] = None


# -------------------------
# SIGN UP STEP 2 (Family)
# -------------------------

class FamilyInfoRequest(BaseModel):

    user_id: int

    family_size: int

    role_in_family: str

    family_space_name: str

    priorities: List[str]
    # ["Saving Money", "Staying Organized", "Sharing Memories", "Staying Connected"]


# -------------------------
# OTP VERIFY
# -------------------------

class VerifyOTPRequest(BaseModel):

    email: EmailStr
    otp: str


# -------------------------
# FORGOT PASSWORD STEP 1
# -------------------------

class ForgotPasswordRequest(BaseModel):

    email: EmailStr


# -------------------------
# FORGOT PASSWORD STEP 2
# -------------------------

class VerifyResetOTPRequest(BaseModel):

    email: EmailStr
    otp: str


# -------------------------
# FORGOT PASSWORD STEP 3
# -------------------------

class ResetPasswordRequest(BaseModel):

    email: EmailStr
    new_password: str