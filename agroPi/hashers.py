from django.contrib.auth.hashers import BCryptSHA256PasswordHasher, check_password, is_password_usable, make_password


class MyBcryptPasswordHasher(BCryptSHA256PasswordHasher):
    def PasswordHasher(password):

        hashed_password = make_password(
            password, salt=None, hasher='bcrypt_sha256')

        verify = check_password(password, hashed_password)

        check = is_password_usable(hashed_password)

        return hashed_password
