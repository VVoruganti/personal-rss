#!/bin/bash

source venv/bin/activate
python rss.py
deactivate

# Use the below for the cron job
# 0 8 * * * ./cron_rss.sh
