# Web Development Coding Test: Next.js Application with Django API Integration  
  
## Objective  

Build a web application using Next.js on the frontend and integrate it with a Django API backend. The application features a basic dashboard page with multiple charts (Candlestick, Line Chart, Bar Chart, and Pie Chart), and the data will be retrieved from the backend.  
  
## Project Structure  
  
The project is organized as a monorepo with two main directories:  
  
- `apps/frontend`: Contains the Next.js frontend application.  
- `apps/server/assignment`: Contains the Django API backend.  
  
## Setup and Installation  
  
### Prerequisites  
  
- [Docker](https://www.docker.com/products/docker-desktop) (for containerization)  
- [Node.js](https://nodejs.org/) (for frontend)  
- [Python](https://www.python.org/downloads/) (for backend)  
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)  
  
### Steps to Run Locally  
  
1. **Clone the repository:**  
  
   ```bash
   git clone https://github.com/rohannsahh/blackhouse.git
   cd blackhouse
  
2. **Install dependencies and start development servers:**     
   ```bash  
   npm install
   npm run dev
  
 This command will:  
   
* Install dependencies for both frontend and backend.  
* Start the Next.js frontend and Django backend concurrently.  
  
## Or Run with Docker  
  
 **Build and start containers:**  
    ```bash
    docker-compose up --build
  
This command will:  
  
* Build Docker images for the frontend and backend.  
* Start the containers for both services.  
* The frontend will be accessible at http://localhost:3000 and the backend at http://localhost:8000.  
  
## Project Details  
  
 **Frontend: Next.js Application**  
  
 * Dashboard Page: Includes four different types of charts:  
  1. Candlestick Chart  
  2. Line Chart  
  3. Bar Chart  
  4. Pie Chart  
 * Chart Library: Recharts  
 * Data Fetching: Using Next.js API routes or fetch/axios calls.  
  
 **Backend: Django API**  
  
 * API Endpoints:  
 1. /api/candlestick-data/ – Returns JSON data for the Candlestick chart.  
 2. /api/line-chart-data/ – Returns JSON data for the Line chart.  
 3. /api/bar-chart-data/ – Returns JSON data for the Bar chart.  
 4. /api/pie-chart-data/ – Returns JSON data for the Pie chart.  
  
* Frontend Implementation: Use of React and Next.js features, integration of charting libraries, data fetching, and code cleanliness.  
* Backend Implementation: Creation of Django APIs, response format, and API handling.  
* Integration: Successful data fetching and error handling.  
* Code Quality: Clean and organized code, proper comments, and best practices.  
* UI/UX: Simple, clean, responsive design with clear data representation.  
  
## Additional Features  
* TypeScript: Used in the Next.js app for type safety.  
* Docker: For easy setup and deployment of both frontend and backend.  
* Testing: Basic unit or integration tests.  
* State Management: Redux or similar for managing frontend data.  
  