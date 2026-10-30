#!/bin/bash
# start this script with 'sudo'

# init colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# update ufw
apt update && apt install -y ufw
echo -e "${GREEN}UFW WAS UPDATED SUCCESSFULY${NC}"

# set opened ports
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow 3096/tcp
echo -e "${GREEN}ALLOW PORTS SETTED SUCCESSFULY${NC}"

# set default rules
ufw default deny incoming
ufw default allow outgoing
echo -e "${GREEN}DEFAULT RULES SETTED SUCCESSFULY${NC}"

# enable ufw
ufw --force enable
echo -e "${GREEN}UFW ENABLED SUCCESSFULY$${NC}"


