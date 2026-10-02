<div align="center">

<h1>🚀 Decode Labs - Project 1: Stateless REST API</h1>

<p>
<img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi">
<img src="https://img.shields.io/badge/Uvicorn-200%20OK-green?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

<p><i>Built by <b>Hamza Shahid</b> | Decode Labs Internship 2026</i></p>

</div>

<hr>

<h2>📌 Project Overview</h2>
<p>This is <b>Project 1</b> of Decode Labs Internship. A fully stateless REST API built with <b>FastAPI</b> that handles user data in-memory with proper HTTP status codes, JSON responses, and error handling.</p>

<h2>🛠️ Tech Stack</h2>
<ul>
<li><b>Framework:</b> FastAPI</li>
<li><b>Server:</b> Uvicorn</li>
<li><b>Language:</b> Python 3.10+</li>
<li><b>Storage:</b> In-Memory List (Stateless)</li>
<li><b>Documentation:</b> Swagger UI / OpenAPI</li>
</ul>

<h2>📁 Project Structure</h2>
<pre>
Decode-Labs-Project-1/
├── project.py
├── README.md
└── screenshots/
    ├── 1_server_running.png
    ├── 2_post_201.png
    ├── 3_get_all_count.png
    ├── 4_get_single_200_and_404.png
    └── 5_browser_users_direct.png
</pre>

<h2>🔌 API Endpoints</h2>
<table>
<tr><th>Method</th><th>Endpoint</th><th>Description</th><th>Status</th></tr>
<tr><td>GET</td><td><code>/users</code></td><td>Get all users with count</td><td>200 OK</td></tr>
<tr><td>POST</td><td><code>/users</code></td><td>Create a new user</td><td>201 Created</td></tr>
<tr><td>GET</td><td><code>/users/{user_id}</code></td><td>Get single user by ID</td><td>200 / 404</td></tr>
<tr><td>GET</td><td><code>/</code></td><td>Root health check</td><td>200 OK</td></tr>
</table>

<h2>🚀 How to Run Locally</h2>
<pre>
# 1. Clone the repo
git clone https://github.com/hamzashahidshahid526-bot/Project-1-at-Decode-Labs.git

# 2. Install dependencies
pip install fastapi uvicorn

# 3. Run the server
uvicorn project:app --reload

# 4. Open in browser
http://127.0.0.1:8000/docs
</pre>


<hr>

<h2>✅ Features Implemented</h2>
<ul>
<li>✔️ Stateless REST architecture</li>
<li>✔️ Proper HTTP status codes: 200, 201, 400, 404, 422</li>
<li>✔️ JSON structured responses with <code>count</code> and <code>data</code></li>
<li>✔️ Duplicate ID validation (400 error)</li>
<li>✔️ User not found handling (404 error)</li>
<li>✔️ Auto-generated Swagger Docs at <code>/docs</code></li>
</ul>

<div align="center">
<h3>⭐ Made for Decode Labs Internship</h3>
<p><b>Intern: Hamza Shahid</b></p>
</div>

