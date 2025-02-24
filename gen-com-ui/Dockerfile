FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY ../package.json ../package-lock.json ./
RUN npm install

# Copy app files
COPY . .

# Build the Next.js app
RUN npm run build

# Expose frontend port
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
