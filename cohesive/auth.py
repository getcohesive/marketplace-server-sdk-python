from dataclasses import dataclass
import datetime

import jwt

from cohesive import app_secret
from cohesive.error import AuthenticationError


@dataclass
class AuthDetails:
    user_id: int
    user_name: str
    role: str
    workspace_id: int
    workspace_name: str
    instance_id: int
    current_period_started_at: datetime.datetime
    current_period_ends_at: datetime.datetime
    is_in_trial: bool


def validate_token(token: str) -> AuthDetails:
    try:
        claims = jwt.decode(token, app_secret, algorithms=["HS256"])
        return AuthDetails(**claims)
    except jwt.exceptions.PyJWTError as e:
        raise AuthenticationError(message=str(e), http_status=None, http_body=None, http_headers=None)
