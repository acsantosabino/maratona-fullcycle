FROM gobuffalo/buffalo

ENV GO111MODULE on
ENV GOPROXY http://proxy.golang.org

EXPOSE 3000
# Bind the app to 0.0.0.0 so it can be seen from outside the container
ENV ADDR=0.0.0.0

WORKDIR /src/app

# # this will cache the npm install step, unless package.json changes

COPY ./app .
RUN yarn install --no-progress
RUN go mod download

ENTRYPOINT [ "buffalo", "dev" ]