# Python Patterns

> Best practices for Python projects using Claude Code

---

## Project Structure

```python
# Prefer explicit imports
from typing import Optional, List, Dict
from dataclasses import dataclass
from pathlib import Path

# Use pathlib over os.path
config_path = Path(__file__).parent / "config.yaml"
```

---

## Type Hints (Always)

```python
def process_user(
    user_id: str,
    options: Optional[Dict[str, Any]] = None
) -> UserResult:
    """Process user with optional configuration."""
    ...
```

---

## Error Handling

```python
# Custom exceptions with context
class ValidationError(Exception):
    def __init__(self, field: str, message: str):
        self.field = field
        super().__init__(f"{field}: {message}")

# Use specific exceptions
try:
    result = api_call()
except requests.Timeout:
    logger.warning("API timeout, retrying...")
    result = api_call_with_retry()
except requests.HTTPError as e:
    logger.error(f"API error: {e.response.status_code}")
    raise
```

---

## Testing with pytest

```python
# Fixtures for reusable setup
@pytest.fixture
def sample_user():
    return User(id="123", name="Test User")

# Parametrized tests for coverage
@pytest.mark.parametrize("input,expected", [
    ("valid@email.com", True),
    ("invalid", False),
    ("", False),
])
def test_email_validation(input: str, expected: bool):
    assert validate_email(input) == expected

# Async testing
@pytest.mark.asyncio
async def test_async_fetch():
    result = await fetch_data()
    assert result is not None
```

---

## FastAPI Patterns

```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, validator

class UserCreate(BaseModel):
    email: str
    name: str

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v.lower()

@app.post("/users", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    # Validation happens automatically via Pydantic
    ...
```

---

## Django Patterns

```python
# Use select_related/prefetch_related to avoid N+1
users = User.objects.select_related('profile').prefetch_related('orders')

# Use F() for atomic updates
from django.db.models import F
Product.objects.filter(id=product_id).update(stock=F('stock') - 1)

# Custom managers for reusable queries
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
```

---

## Logging (Not Print)

```python
import logging

logger = logging.getLogger(__name__)

# Use appropriate levels
logger.debug("Detailed info for debugging")
logger.info("Normal operation info")
logger.warning("Something unexpected but handled")
logger.error("Error occurred", exc_info=True)

# Never log sensitive data
logger.info(f"Processing user {user_id}")  # OK
logger.info(f"User password: {password}")  # NEVER
```

---

## Environment & Config

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    api_key: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()  # Auto-loads from environment
```

---

## Async Best Practices

```python
import asyncio
import aiohttp

# Gather for parallel execution
async def fetch_all(urls: List[str]) -> List[dict]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Use async context managers
async with aiofiles.open('file.txt', 'r') as f:
    content = await f.read()
```

---

## Security

```python
# Use secrets for tokens
import secrets
token = secrets.token_urlsafe(32)

# Hash passwords properly
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"])
hashed = pwd_context.hash(password)

# Parameterized queries (SQLAlchemy)
session.execute(
    text("SELECT * FROM users WHERE id = :id"),
    {"id": user_id}
)
```
