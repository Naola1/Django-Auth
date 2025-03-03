# Django Authentication App with JWT

This Django authentication system provides a robust solution for modern web applications, featuring JWT authentication, social login (Google, Facebook, GitHub), email verification, and user profile management. Built with django-rest-auth and django-allauth.

## Features

- User registration and login
- JWT token authentication
- Token refresh functionality
- Token rotation & blacklisting
- Social Authentication (Google, Facebook, GitHub)
- Email verification & password reset
- User profile management
- Secure session management
- Mobile-ready API endpoints

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Naola1/django-jwt-auth.git
   cd django-jwt-auth
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables (create a `.env` file in the project root):
   ```
   # Django
   SECRET_KEY=your-secure-key-here
   DEBUG=True

   # JWT
   JWT_SECRET_KEY=your-jwt-secret-key

   # Email settings
   EMAIL_HOST_USER=your-email-address
   EMAIL_HOST_PASSWORD=your-email-account-password

   # Google OAuth
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret

   # Facebook OAuth
   FACEBOOK_APP_ID=your-facebook-app-id
   FACEBOOK_APP_SECRET=your-facebook-app-secret

   # GitHub OAuth
   GITHUB_CLIENT_ID=your-github-client-id
   GITHUB_CLIENT_SECRET=your-github-client-secret
   ```

5. Run migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login with username/password
- `POST /api/auth/refresh/` - Refresh JWT token
- `POST /api/auth/verify/` - Verify JWT token
- `POST /api/auth/logout/` - Logout (invalidate token)

### Social OAuth

#### Google OAuth
- `GET /api/auth/google/login/` - Get Google OAuth authorization URL
- `POST /api/auth/google/callback/` - Handle Google OAuth callback
- `POST /api/auth/google/token/` - Login with Google access token

#### Facebook OAuth
- `GET /api/auth/facebook/login/` - Get Facebook OAuth authorization URL
- `POST /api/auth/facebook/callback/` - Handle Facebook OAuth callback
- `POST /api/auth/facebook/token/` - Login with Facebook access token

#### GitHub OAuth
- `GET /api/auth/github/login/` - Get GitHub OAuth authorization URL
- `POST /api/auth/github/callback/` - Handle GitHub OAuth callback
- `POST /api/auth/github/token/` - Login with GitHub access token

### User Profile

- `GET /api/users/me/` - Get current user profile
- `PUT /api/users/me/` - Update current user profile
- `PATCH /api/users/me/` - Partially update current user profile

### Password Management

- `POST /api/auth/password/reset/` - Request password reset
- `POST /api/auth/password/reset/confirm/` - Confirm password reset
- `POST /api/auth/password/change/` - Change password (authenticated users)

## Authentication Flow

### Traditional Authentication

1. Register a user with `POST /api/auth/register/`
2. Login with `POST /api/auth/login/` to receive JWT tokens
3. Include the access token in the Authorization header for subsequent requests:
   ```
   Authorization: Bearer <access_token>
   ```
4. Refresh the token with `POST /api/auth/refresh/` when it expires

### Social OAuth Authentication

1. Get the authorization URL from:
   - Google: `GET /api/auth/google/login/`
   - Facebook: `GET /api/auth/facebook/login/`
   - GitHub: `GET /api/auth/github/login/`
2. Redirect the user to the provided URL.
3. After user consent, the provider redirects to your callback URL with an authorization code.
4. Exchange the code for tokens with:
   - Google: `POST /api/auth/google/callback/`
   - Facebook: `POST /api/auth/facebook/callback/`
   - GitHub: `POST /api/auth/github/callback/`
5. Or, if you already have an access token, use:
   - Google: `POST /api/auth/google/token/`
   - Facebook: `POST /api/auth/facebook/token/`
   - GitHub: `POST /api/auth/github/token/`

## Testing with Postman

You can import the included Postman collection to test all API endpoints:

1. Import `Django_JWT_Auth.postman_collection.json` into Postman
2. Set up environment variables in Postman:
   - `base_url`: Your API base URL (e.g., `http://localhost:8000/api`)
   - `access_token`: Will be automatically set after login
   - `refresh_token`: Will be automatically set after login

## Security Considerations

- Store your JWT secret key securely
- Set appropriate token lifetimes
- Use HTTPS in production
- Keep OAuth credentials confidential
- Implement rate limiting for authentication endpoints
- Consider implementing IP-based blocking for suspicious activity

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.