#!/usr/bin/env bash
# Enter the persistent Jazzy container "my_bot", creating it (and the image) on first use.
#   - container doesn't exist -> build image if needed, create container, open a shell
#   - container stopped       -> start it again and open a shell
#   - container running       -> open another shell in it
# Usage:  ./docker/run.sh                -> GPU rendering via /dev/dri
#         SOFTWARE_GL=1 ./docker/run.sh  -> CPU rendering (only takes effect when the container is created)
# Start fresh:  docker rm -f my_bot && ./docker/run.sh
set -e

IMAGE=my_bot:jazzy
NAME=my_bot
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WS_DIR="$(cd "$SCRIPT_DIR/../../.." && pwd)"   # .../catkin_ws (contains src/my_bot)

xhost +local:docker >/dev/null   # let the container open windows on your X display (needed every login)

if docker container inspect "$NAME" >/dev/null 2>&1; then
    if [ "$(docker container inspect -f '{{.State.Running}}' "$NAME")" != "true" ]; then
        docker start "$NAME" >/dev/null
    fi
    exec docker exec -it "$NAME" bash
fi

if ! docker image inspect "$IMAGE" >/dev/null 2>&1; then
    docker build -t "$IMAGE" "$SCRIPT_DIR"
fi

GL_ENV=()
if [ "${SOFTWARE_GL:-0}" = "1" ]; then
    GL_ENV=(-e LIBGL_ALWAYS_SOFTWARE=1)
fi

docker run -dit \
    --name "$NAME" \
    --net=host --ipc=host \
    -e DISPLAY="$DISPLAY" \
    -e QT_X11_NO_MITSHM=1 \
    "${GL_ENV[@]}" \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    --device /dev/dri \
    --group-add video --group-add "$(getent group render | cut -d: -f3 | grep . || echo video)" \
    -v "$WS_DIR":/ws \
    "$IMAGE"

exec docker exec -it "$NAME" bash
