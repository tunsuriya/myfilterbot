#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = "6935152"

API_HASH = os.environ.get("56388e5ff61096e112a54dbe7c7d56e5")

BOT_TOKEN = os.environ.get("2140123902:AAEGnA4vkWJAUlZXKWAdFNHXQ2J_jUR25nk")

DB_URI = os.environ.get("mongodb+srv://adminmty:mtyadmin@cluster0.khuro.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("USER_SESSION")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
