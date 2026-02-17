#!/bin/bash

# Setup script for kb-mathematics project
# This script creates a virtual environment, activates it, and installs dependencies
#
# Usage:
#   source setup.sh    # Recommended - activates venv in current shell
#   . setup.sh         # Alternative syntax (same as source)

set -e  # Exit on error

# Check if script is being sourced (required for venv activation)
# Exit with error if script is executed directly instead of sourced
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "Error: This script must be sourced, not executed directly."
    echo ""
    echo "Usage:"
    echo "  source setup.sh"
    echo "or"
    echo "  . setup.sh"
    echo ""
    exit 1
fi

# Check if git is available
if ! command -v git &> /dev/null; then
    echo "Error: git is not installed or not in PATH."
    exit 1
fi

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: This project is not controlled by git. Please initialize git first."
    exit 1
fi

# Determine project root using git
PROJECT_ROOT=$(git rev-parse --show-toplevel)
if [ -z "$PROJECT_ROOT" ]; then
    echo "Error: Could not determine project root from git repository."
    exit 1
fi

# If virtual environment does not exist, create it
if [ ! -d "${PROJECT_ROOT}/.venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "${PROJECT_ROOT}/.venv"
    echo "Virtual environment created successfully!"
fi

# Activate virtual environment
source "${PROJECT_ROOT}/.venv/bin/activate"

# Install dependencies if requirements.txt exists
if [ -f "${PROJECT_ROOT}/requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r "${PROJECT_ROOT}/requirements.txt"
else
    echo "Warning: requirements.txt not found. Skipping dependency installation."
fi

echo "Setup complete! Virtual environment is activated."

