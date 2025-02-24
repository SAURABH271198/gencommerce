FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy monorepo-wide package files
COPY ../package.json ../package-lock.json ./

# Install dependencies from monorepo root
RUN npm install

# Copy the entire monorepo (so it includes shared libs)
COPY . .

# Build the Next.js app
WORKDIR /app/apps/gen-com-ui
RUN npm run build

# Expose frontend port
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
