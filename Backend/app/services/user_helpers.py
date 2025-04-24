from abc import ABC

from app.model.repository.user_repository import UserRepository


class UserHelpers(ABC):
    def get_user_data_from_token(token):
        """Mock function to simulate user token validation."""
        return UserRepository.get_user_from_token(token)