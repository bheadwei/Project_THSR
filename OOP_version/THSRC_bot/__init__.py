# __init__.py

"""
THSRC_Bot_Package
高鐵訂票的各項功能模組
"""

# 導入瀏覽器
from .browser import create_browser

#導入booking主要功能
from .booking import THSRCBot

#導入識別碼功能
from .ocr import CaptchaSolver

#導入訂票資訊功能
from .parser import BookingInfoParser

__all__ = [
    "create_browser",
    "THSRCBot",
    "CaptchaSolver",
    "BookingInfoParser",
]
