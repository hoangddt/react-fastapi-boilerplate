## Task 1. Create the Timeline List Page

Create a component to display a list of timeline entries in chronological order. Each entry should be presented as a card, showing media, title and text description, with a user-friendly design.

Requirements:

1. Data of timeline entries will be fetched from backend API, currently there are no backend, so please put a placeholder for backend call and instead return some mock data for rendering the pages.
2. Timeline entries must be display vertially, and paginate for each 20 entries per page.
3. The media should be display via a carousel
4. Make the title clickable, and when click, it leads to timeline detail view page

## Task 2. Create timeline detail page

As a user, I want to click on a timeline event and see a detailed view (with full-length media, complete description, and event details) so that I can get more context about the event.

Requirements:

1. Detail view will be a separated page with separated route, with id in the route
2 The detail view need to display: 
- The title, a full description, and time details.
- A larger display of media. If there are multiple images/videos, provide a carousel or a gallery view.
3. User be able to edit the title, description, and media files
4. Send edit payload to backend, since there are no backend yet, please mock a backend call and assume the call sucessfully, use console.log to log the action
5. There must be a back button for the user to go back to the feed

## Task 3. Create the Timeline Event Creation page

As a user, I want to be able to add a new timeline event with a title, media attachments, and a short description so that I can update and enrich my timeline.

Requirements:
1. When user click button "Create new timeline" it will lead to this page
2. The form displays fields for the title (text input), media upload (supporting multiple selections for images/videos), and a description (textarea).
3. On form submission, the event is sent to the backend, and once confirmed, it gets immediately added to the timeline feed. Since there is no backend yet, please put a placeholder and assume the operation success
4. Upon success creation, redirect back to homepage feed


## Task 4. Create FastAPI endpoint for upload static files

As a user, i want to upload static file and can received its id and absolute url path so I can reference them or used to display.

Requirements:

1. Create an API Endpoint for user to upload the static file, when the server received the file, it will storage in supabase storage (using supabase storage client).
2. After successfully save to supabase, insert an entry to tl__static_file table. Then return the created entry
3. Create an API that the user can just pass the id of the file and can get JSON response of file data inside tl__static_file table
4. We dont use SQL database but use table in Supabase, all table are created, please use it via Supabase client

## Task 5. Build FastAPI Backend Endpoints for Timeline CRUD

I want the backend to support creating new timeline events and retrieving them (CRUD operations) so that the timeline feed is powered by a reliable API and the events are stored in Supabase.

Requirements:
1. The frontend event details (title, description, media URLs) to the FastAPI endpoint.
2. A GET request is available for fetching all timeline events for the authenticated user, sorted chronologically.
3. Create endpoints for get, update, delete one timeline entry
4. The API will return JSON responses that the frontend can consume
5. Ensure proper HTTP status codes and error messages to support a smooth UX on the frontend.
6. Connect FastAPI with Supabase as the database backend (this might involve using the Supabase Python client). All tables are created in supabase already

## Task 6. Integrate frontend & backend for timeline data operations

As a user, when I create or view timeline events, I want the frontend to seamlessly fetch and display data from the backend so that my timeline is always up-to-date.

Requirements:

0. The backend is ready and up and running, now wire the placeholder in the frontend to actual backend call. Please set variable to backend root url and use it to concatenate for the endpoint
1. Update the timeline listing page to actually call to backend API instead of mockdate
2. Update the timeline detail view page to also call to Backend API, wire update, delete action with the API
3. Update the timeline creation page to wire to the backend API

## Task 6: Update the field of timeline entries

The timeline is work now, but some fields are left unused, i want to enable these field for user input as well as display them.

Requirements:
1. Update to use start_time, end_time and tags. Where:
- start_time: is the time of the event start
- end_time: is the time of the event end, this field is optional
- tags: is tags of the event, this also optional
2. Update the creation, edit pages to include those fields
3. Update list view and detail view page to also include those fields
4. Make sure to make changes on both frontend and backend

## Task 7: Add user authentication API suites

I want to make sure that every action on the system are tied to a specific user.

Requirements:
1. Create a API suites for user authentication: sign up, sign in, forgot password, update profile, get current user information. To make it simple, use email and password for credential for now. Extra user information is: username and full name.
2. Replace the current user api module, I want to use supabase for user management backend, please change to use it instead.
3. Make change to the API first, and write a short instruction on how the frontend include logged in information for API request

## Task 8: Add user authentication in the frontend pages

Now we have the user authentication API, i want to integration full user authentication in the frontend, including sign up, sign in, forgot password and guard route that is public and private

Requirements:
1. User authentication API already set up in the backend, now create pages to wire to the backend.
2. Required pages:
    - Sign up page: user be able to register by email and password. After sign up, they will be redirect to login
    - Login page: User input email and password to login, after the user log in, make sure to save the JWT access token for later query. Redirect user to homepage when they login succesfullt
    - Forgot password: User can input email to request password reset
    - Profile page: user can view their profile information, and can update username, fullname, as well as password
3. Update so the homepage, timeline related page and profile page require authentication
4. When user successfully login, their token need to include to every request to backend, it will be in the header will key, value as: "Authorization", "Bearer {{jwt_token}}"

## Task 9: Update authentication header when query timeline endpoints:

The timeline endpoints require authentication, can you update to also include the authentication header, just like query for profiles


## Task x. Change to s3 storage for cheaper and more longtime pricing save

Future plan, no implementation yet at this moment
