#!/usr/bin/env python3
"""
Authentication Module
"""

from flask import request
from typing import TypeVar, List


class Auth:
    """
    Auth class to manage API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        public method require_auth
        """
        if path[-1] != '/':
            path += '/'
        if path not in excluded_paths or path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """
        public method authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        public method current_user
        """
        return None
