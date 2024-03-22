FROM node:20 as build-stage
WORKDIR /usr/src/app
COPY ["frontend/package.json", "/usr/src/app/"]
COPY ["frontend/yarn.lock", "/usr/src/app/"]
RUN yarn

COPY ["./frontend", "./"]

CMD ["yarn", "jest"]