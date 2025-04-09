# Facial Enhancement Visualiser
A web application that uses AI (StyleGAN) to visualize potential cosmetic enhancements on facial images.

# Project Overview
This system allows users to:

- Upload a photo of their face
- Select desired facial feature enhancements (e.g., smoother skin, reduce wrinkles)
- View a realistic visualization of how they might look after such enhancements
- Compare before/after images and download results

# Architecture
The system consists of:

- **Frontend**: User interface built with HTML/CSS/JavaScript
- **Backend API**: FastAPI service for handling requests
- **Model Server**: StyleGAN2-ADA deployed as a service for image generation
- **Infrastructure**: Docker containers orchestrated with Kubernetes
