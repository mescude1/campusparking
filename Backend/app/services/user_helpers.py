from abc import ABC


class UserHelpers(ABC):
    def get_user_data_from_token(token):
        """Mock function to simulate user token validation."""
        return USERS.get(token)