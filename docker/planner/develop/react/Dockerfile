# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM node:20 as build-stage
WORKDIR /usr/src/app
COPY ["frontend/package*.json", "/usr/src/app/"]
RUN yarn

CMD ["yarn", "dev"]