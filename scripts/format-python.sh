#!/usr/bin/env bash

set -euo pipefail

# Go to script directory
cd "$(dirname "$0")"

uvx black *.py
