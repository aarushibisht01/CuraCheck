#!/usr/bin/env bash
# Build script for Render

echo "Installing Python dependencies..."
pip install -r backend/requirements.txt

echo "Setting up model directory..."
mkdir -p backend/models

echo "Build completed successfully!"
