#!/bin/bash
searchsploit --nmap $1 -j > ploit.json
python searchploit2faraday.py > $2
echo 'done'