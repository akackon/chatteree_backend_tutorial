from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("sign-in")
def sign_in():
    return "Sign in"


@auth.route("verify-your-number")
def verify_your_number():
    return "Verify your number"


@auth.route("verify-your-number-error")
def verify_your_number_error():
    return "Verify your number error"


@auth.route("chatteree-id")
def chatteree_id():
    return "Chatteree ID"


@auth.route("chatteree-id-checking")
def chatteree_id_checking():
    return "Chatteree ID checking"


@auth.route("chatteree-id-good")
def chatteree_id_good():
    return "Chatteree ID good"


@auth.route("chatteree-id-bad")
def chatteree_id_bad():
    return "Chatteree ID bad"


@auth.route("set-up-profile")
def set_up_profile():
    return "Set up profile"

@auth.route("set-up-profile-provided")
def set_up_profile_provided():
    return "Set up profile provided"


