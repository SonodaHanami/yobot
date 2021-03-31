import json
import os
import random
import re
import requests
from datetime import datetime, timedelta
from hashlib import sha256
from random import randint as ri


class Kusa:
    def __init__(self, **kwargs):
        pass

    async def execute_async(self, message):
        msg = message['raw_message'].strip()
        group = str(message.get('group_id', ''))
        user = str(message.get('user_id', ''))

        if msg.startswith('草'):
            if ri(1, 4) == 1:
                return '草'
            elif ri(1, 9) == 1:
                return '草.jpg'