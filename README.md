# FastAPI/Supabase Todo App

## DB Setup

### Create an ENUM type for status
CREATE TYPE status_enum AS ENUM ('todo', 'in_progress', 'done');

### Create the Todo table
CREATE TABLE todo (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT DEFAULT 'No description',
    created_at TIMESTAMP NOT NULL,
    edited_at TIMESTAMP NOT NULL,
    status status_enum NOT NULL
);

### Create the Note table
CREATE TABLE note (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    edited_at TIMESTAMP NOT NULL
);