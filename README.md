# Project posts

## Features

- User authentication
- Posting messages
- Retrieving messages
- Updating messages
- Deleting messages

## API Endpoints

### Auth

- `POST /auth/sign_up`: Endpoint for user registration.
- `POST /auth/sign_in`: Endpoint for user login.

### Posts

- `POST /posts/`: Create a new post.
- `GET /posts/`: Retrieve a list of posts.
- `GET /posts/{post_id}`: Retrieve a post by ID.
- `PUT /posts/{post_id}`: Update a post by ID.
- `DELETE /posts/{post_id}`: Delete a post by ID.

### Documentation
For full API documentation and testing endpoints, navigate to /docs or /redoc paths on the running FastAPI server.

## Getting Started

### Prerequisites

- Python 3.8 or newer
- Pip package manager

### Installing

```bash
# Clone the repository
git clone https://github.com/rustamrv/fast_api_posts

# Navigate to the project directory
cd fast_api_posts

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app  --reload