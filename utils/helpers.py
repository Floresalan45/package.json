"""Helper functions for the bot"""

import re
from typing import Optional

def format_lua_code(code: str) -> str:
    """Format Lua code for display"""
    # Remove extra whitespace
    code = re.sub(r'\n\s*\n', '\n', code).strip()
    return code

def truncate_text(text: str, max_length: int = 1024) -> str:
    """Truncate text to max length"""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."

def validate_lua_syntax(code: str) -> bool:
    """Basic Lua syntax validation"""
    # Check for basic Lua keywords
    keywords = ['function', 'end', 'if', 'then', 'local', 'return']
    
    # Check if code contains at least basic structure
    has_keywords = any(keyword in code.lower() for keyword in keywords)
    
    # Check for matching brackets
    if code.count('(') != code.count(')'):
        return False
    
    return True

def split_into_chunks(text: str, chunk_size: int = 1024) -> list:
    """Split text into chunks of specified size"""
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks
