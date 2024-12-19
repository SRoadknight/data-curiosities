# Use Nginx to serve the built files
FROM nginx:alpine

# Copy the built files from the first stage
COPY dist /usr/share/nginx/html