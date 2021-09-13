from functions import storage
import os, sys, toml

with open("config.toml") as file:
    config = toml.load(file)["sessions"]

sessions = storage.sessions("sessions", api_id, api_hash)
