# User Authentication Microservice

## Endpoints
- **Register:** `POST /register`
- **Login:** `POST /login`
- **Profile:** `GET /profile` (Requires Authorization)

### **Request Examples:**

#### **1. Registration:**
```bash
curl -X POST https://your-vercel-url/register \
-H "Content-Type: application/json" \
-d '{"username": "testUser", "password": "password123"}'
