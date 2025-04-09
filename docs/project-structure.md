# Create a file documenting the structure
echo "# Project Structure

## Overview
This document outlines the structure of the Facial Enhancement Visualizer project.

## Directories
- \`.github/workflows\`: CI/CD configuration
- \`backend/\`: FastAPI backend service
  - \`app/\`: Application code
- \`frontend/\`: React frontend application
  - \`public/\`: Static assets
  - \`src/\`: React source code
    - \`components/\`: Reusable UI components
    - \`pages/\`: Page components
    - \`services/\`: API service classes
    - \`utils/\`: Utility functions
    - \`assets/\`: Images and other assets
    - \`styles/\`: CSS and styling files
- \`model/\`: StyleGAN model service
- \`kubernetes/\`: Kubernetes configuration
- \`docker/\`: Docker configurations
- \`docs/\`: Project documentation
- \`scripts/\`: Utility scripts

## Configuration Files
- \`environment.yml\`: Conda environment configuration
- \`docker-compose.yml\`: Docker Compose configuration
- \`.env\`: Environment variables (not versioned)
- \`package.json\`: Frontend dependencies