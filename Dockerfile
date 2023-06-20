# Use the official Node.js image as the base
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY sample-react-app .

# Build the React app
RUN npm run build

# Expose the desired port (e.g., 3000) for the application
EXPOSE 3000

# Start the application
CMD ["npm", "start"]
