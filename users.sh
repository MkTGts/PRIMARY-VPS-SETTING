#!/bin/bash
# start this script with 'sudo'

# init colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# add a user and permissions
adduser username
usermod -aG sudo username