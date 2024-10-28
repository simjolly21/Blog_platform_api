# Blog_platform_api

This is the project link: https://roadmap.sh/projects/blogging-platform-api

## Running the Application

1. Initialize the Database: Run the app once to set up the `blog.db` SQLite file.

        python app.py

2. Use an API client like Postman or curl to test each endpoint.

## Testing Endpoints
- Create a new post: `POST /posts`
- Update a post: `PUT /posts/<post_id>`
- Delete a post: `DELETE /posts/<post_id>`
- Get a post: `GET /posts/<post_id>`
- Get all posts: `GET /posts`
- Search posts: `GET /posts?term=<search_term>`

This basic blogging platform API enables CRUD operations, filtering, and uses best practices for statsu codes and error handling, making it easily extensible with authentication and pagination in the future. Let me know if you need further customizations or explanations on specific sections!
