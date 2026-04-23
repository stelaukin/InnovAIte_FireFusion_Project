"""
Client wrapper for LLM providers (Gemini by default) used in narrative clustering.

This module handles API authentication, model initialization, prompt submission,
and response parsing (text/JSON), so higher-level pipeline code can focus on
grouping social media posts into similar narratives.
"""

import json
import os
import time
from dataclasses import dataclass
from typing import Any, Optional

import google.generativeai as genai


@dataclass
class GeminiConfig:
    """Configuration for Gemini client behavior."""
    model_name: str = "gemini-1.5-pro"
    api_key_env: str = "GEMINI_API_KEY"
    temperature: float = 0.2
    max_output_tokens: int = 1024
    top_p: float = 0.95
    top_k: int = 40
    timeout_seconds: int = 30
    max_retries: int = 3
    retry_backoff_seconds: float = 1.5


class GeminiClient:
    """
    Thin wrapper over Gemini SDK.

    Initial responsibilities:
    - Initialize API client
    - Generate plain text responses
    - Generate JSON-like structured responses
    - Handle retries and common exceptions
    """

    def __init__(self, config: Optional[GeminiConfig] = None, api_key: Optional[str] = None) -> None:
        self.config = config or GeminiConfig()
        self.api_key = api_key or os.getenv(self.config.api_key_env)

        if not self.api_key:
            raise ValueError(
                f"Gemini API key not found. Set env var `{self.config.api_key_env}` "
                "or pass `api_key` explicitly."
            )

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.config.model_name)

    # Finish the remaining based on the project's objectives
    
