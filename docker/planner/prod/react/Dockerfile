# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM node:20 as build-stage
WORKDIR /usr/src/app
COPY ["frontend/package*.json", "/usr/src/app/"]
RUN yarn
COPY ["./", "/usr/src/app/"]
RUN yarn build

FROM nginx:1
COPY --from=build-stage ["/usr/src/app/frontend/dist/",  "/usr/share/nginx/html"]
COPY ["./docker/prod/react/nginx.conf", "/etc/nginx/conf.d/default.conf"]
COPY ["./docker/prod/react/nginx-backend-not-found.conf", "/etc/nginx/extra-conf.d/backend-not-found.conf"]
