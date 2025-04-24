from flask import session
from src.Database import Database

db = Database.get_connection()
users_collection = db.register

class Auth:
    @staticmethod
    def email_exists(email):
        """Check if an email already exists in the database."""
        return users_collection.find_one({"email": email}) is not None

    @staticmethod
    def register(full_name, email, password):
        """Registers a new user if they don't already exist."""

        if Auth.email_exists(email):
            return "User already exists"
        # Store user details in session
        session["full_name"] = full_name
        session["email"] = email

        # Insert new user into the database
        users_collection.insert_one({
            "full_name": full_name,
            "email": email,
            "password": password  # Store hashed password
        })
        return "Registration successful"

    @staticmethod
    def login(email, password):
        """Logs in a user if credentials are correct."""
        user = users_collection.find_one({"email": email})

        if user:
            # Check if the password matches (plain text comparison)
            if user["password"] == password:
                session["authenticated"] = True
                session["email"] = email
                return "Login successful"
            else:
                return "Wrong password"
        return "User not found"

