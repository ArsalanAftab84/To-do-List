-- Initialize the database with proper settings
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_todo_created_at ON todo(created_at);
CREATE INDEX IF NOT EXISTS idx_todo_completed ON todo(completed);

-- Set up proper permissions
GRANT ALL PRIVILEGES ON DATABASE todo_db TO postgres;
