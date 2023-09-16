FROM node:20.6

WORKDIR /app

# Copy JSON Package Configuration to install dependencies
COPY package.json .

# Install Dependencies
RUN npm i

# Copy relevant files and directories
COPY public/ ./public
COPY src/ ./src
COPY index.html .
COPY vite.config.js .

# This is the port that Vite sues by default in the vite config file
EXPOSE 5173

# Note, in the package.json file, make sure to include 'vite --host' in the 'dev' script so that the container can be exposed
CMD ["npm", "run", "dev"]
