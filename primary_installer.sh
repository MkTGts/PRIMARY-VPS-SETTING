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
apt install mc htop nano curl wget net-tools dnsutils telnet git nmap ufw -y  
echo -e "${GREEN}THE UTILS UPDATE WAS SUCCESSFUL${NC}"
