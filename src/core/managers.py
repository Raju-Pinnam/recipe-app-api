from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username,
                    password=None,
                    **extra_kwargs):
        """Creates New User with above details
        and **extra_kwargs are more details"""
        if not email:
            raise ValueError("Email cant be empty")
        email = self.normalize_email(email)
        user_obj = self.model(email=email,
                              username=username,
                              **extra_kwargs)
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, username, password=None, **extra_kwargs):
        """Creating super user by reusing create_user function"""
        super_user_obj = self.create_user(email=email,
                                          username=username,
                                          password=password,
                                          **extra_kwargs)
        super_user_obj.is_staff = True
        super_user_obj.is_superuser = True
        super_user_obj.save(using=self._db)
        return super_user_obj
