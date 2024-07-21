
# Authetication System

 A basic user authentication and management system using Django.

## Features

 **User Registration/Sign-up:**
 Users can register with a username, email, and password.

**Login:**
 Registered users can log into the system using their username, email, and password.

**Forgot Password:**
 Users can request a password reset link to their email address.

**Password Reset:**
Users can reset their password using the password reset link sent to their email address.

**Dashboard:** A dashboard view is provided for logged-in users, displaying their usernames.

**Profile:** A profile view is provided for logged-in users, displaying their username, email, date joined, and last login.

**Change Password:** Logged-in users can change their password using a password change form.


## Implementation Choices

- **Django's Built-in Authentication System:** Django's built-in authentication system is used to handle user authentication, password reset, and password change.

- **Custom Views and Forms:** Custom views and forms are created to handle user registration, login, and password reset. This allows us to customize the user experience and add additional functionality as needed.

- **Template-based Views:** We used template-based views to render HTML templates for each view. This allows us to separate the presentation layer from the business logic and makes it easier to maintain and update the UI.

- **Token-based Password Reset** When a user requests a password reset, a token is generated using Django's built-in default_token_generator. This token is sent to the user's email address, along with a URL-safe base64-encoded representation of the user's primary key (uidb64). The token is valid for a limited time and can only be used once.

- **Email Verification:** When a user signs up, an email verification link is sent to their email address. The user must click on this link to activate their account. This helps to prevent spam accounts and ensures that users have a valid email address.


##  Additional Instructions

**Email Configuration:** Make sure to configure Gmail SMTP settings correctly. If you have two-factor authentication (2FA) enabled on your Gmail account, generate an app-specific password and use it in place of your regular Gmail password.
