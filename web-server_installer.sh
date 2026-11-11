#!/bin/bash
# start this script with 'sudo'

# init colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# updating apt
apt update && apt upgrade -y  
echo -e "${GREEN}THE APT UPDATE WAS SUCCESSFUL${NC}"

# installing primaty utils
apt install nginx python3 python3-pip python3-venv postgresql certbot -y  
echo -e "${GREEN}THE UTILS UPDATE WAS SUCCESSFUL${NC}"
