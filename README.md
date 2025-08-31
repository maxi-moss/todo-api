# Todo API

A FastAPI-based todo management application with Supabase backend.

## Features

- CRUD operations for todos
- Status tracking (todo, in_progress, done)
- Supabase database integration

## Setup

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   uv venv
   uv sync
   ```

3. Set up environment variables:
   ```bash
   # Create .env file with:
   CORS_ALLOWED_ORIGINS=http://localhost:5173
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_anon_key
   ```

### Database Setup

Run these SQL commands in your Supabase SQL editor:

```sql
-- Create an ENUM type for status
CREATE TYPE status_enum AS ENUM ('todo', 'in_progress', 'done');

-- Create the Todo table
CREATE TABLE todo (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT DEFAULT 'No description',
    created_at TIMESTAMP NOT NULL,
    edited_at TIMESTAMP NOT NULL,
    status status_enum NOT NULL
);

-- Create the Note table
CREATE TABLE note (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    edited_at TIMESTAMP NOT NULL
);
```

## Running the Application

Start the development server:
```bash
cd src
uvicorn main:app --reload
```

## API Endpoints

- `POST /api/todo/create` - Create a new todo
- `GET /api/todo/get` - Get todo by ID
- `POST /api/todo/update` - Update a todo
- `POST /api/todo/delete` - Delete a todo