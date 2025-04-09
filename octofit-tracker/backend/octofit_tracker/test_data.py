# Test data for populating the octofit_db database

test_users = [
    {"username": "john_doe", "email": "john@example.com", "password": "password123"},
    {"username": "jane_doe", "email": "jane@example.com", "password": "password123"},
]

test_teams = [
    {"name": "Team Alpha", "members": ["john_doe", "jane_doe"]},
]

test_activities = [
    {"user": "john_doe", "activity_type": "Running", "duration": "00:30:00"},
    {"user": "jane_doe", "activity_type": "Cycling", "duration": "01:00:00"},
]

test_leaderboard = [
    {"user": "john_doe", "score": 100},
    {"user": "jane_doe", "score": 150},
]

test_workouts = [
    {"name": "Morning Yoga", "description": "A relaxing yoga session to start the day."},
    {"name": "HIIT", "description": "High-intensity interval training for fat burning."},
]
