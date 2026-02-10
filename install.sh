#!/bin/bash

cd $(dirname $0)/firmware/filesystem
mpremote "$@" cp -r . :
