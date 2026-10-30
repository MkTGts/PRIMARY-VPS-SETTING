#!/bin/bash
# start this script with 'sudo'

# init colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# updating apt
apt update 
echo -e "${GREEN}THE APT UPDATE WAS SUCCESSFUL${NC}"

# install ssh
apt install ssh
echo -e "${GREEN}SSH INSTALLED SUCCESSFUL${NC}"

