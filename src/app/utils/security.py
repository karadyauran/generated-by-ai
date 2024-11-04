from werkzeug.security import generate_password_hash, check_password_hash

# Function to hash a password

def hash_password(password: str) -> str:
    """Generate a hashed password."""
    return generate_password_hash(password)

# Function to verify a password against its hash

def verify_password(password: str, hashed_password: str) -> bool:
    """Verify the password against the hashed password."""
    return check_password_hash(hashed_password, password)