#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(2367149)

API_HASH = "cea7e5b5bbc1c6fca2732288e4a4c49c"

BOT_TOKEN = "1753304211:AAEQ4yfKV4fnp2Jv97S148S6NrNeg4pv_Dw"

DB_URI = "mongodb+srv://mtytgauto:pwdtgauto@cluster0.o9tbd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

USER_SESSION = "BQC7wAluc5TQdiy6hsclF6xqFvdK4P7wkdpCMTGagjLKEbMgdDkMKnSp6MZqDtxY7joBme33t3Yt7IKpyPlbYiMatz0i2ViQTNa2hoRvFPkI2EBIYQVgHqMAsIyV1w5KnTnNlLggamlzZXux7lf2k9d0fymVL4XO25LnxYpvABS0A8MiCncQSuVkbiMZX3xjKRkxPCgQY3uhWC6pjV0iKpMWmn8wi-RHS-duRoGZyOxgW9cRI0tyOi0Kjvpb7KNwOeOBMo6vMDQvRLzoVIs7D_Fmo8dobttdXr1guv5WcqTTO5bq3nqWCgs141mbpNrt-c2ane1_EYEDVk13TkAGl833V8VHPgA"

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
