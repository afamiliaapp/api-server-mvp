from fastapi import APIRouter
from app.schemas.auth_schema import (
    SignInRequest,
    SignUpRequest,
    FamilyInfoRequest,
    VerifyOTPRequest,
    ForgotPasswordRequest,
    VerifyResetOTPRequest,
    ResetPasswordRequest
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# -------------------------
# SIGN IN
# -------------------------

@router.post("/signin")
def signin(payload: SignInRequest):

    return {"message": "signin endpoint"}


# -------------------------
# SIGN UP STEP 1
# -------------------------

@router.post("/signup")
def signup(payload: SignUpRequest):

    return {"message": "signup step 1"}


# -------------------------
# SIGN UP STEP 2
# -------------------------

@router.post("/signup/family")
def signup_family(payload: FamilyInfoRequest):

    return {"message": "signup step 2"}


# -------------------------
# OTP VERIFY
# -------------------------

@router.post("/verify-otp")
def verify_otp(payload: VerifyOTPRequest):

    return {"message": "otp verified"}


# -------------------------
# FORGOT PASSWORD STEP 1
# -------------------------

@router.post("/forgot-password")
def forgot_password(payload: ForgotPasswordRequest):

    return {"message": "otp sent"}


# -------------------------
# FORGOT PASSWORD STEP 2
# -------------------------

@router.post("/verify-reset-otp")
def verify_reset_otp(payload: VerifyResetOTPRequest):

    return {"message": "otp verified"}


# -------------------------
# FORGOT PASSWORD STEP 3
# -------------------------

@router.post("/reset-password")
def reset_password(payload: ResetPasswordRequest):

    return {"message": "password updated"}