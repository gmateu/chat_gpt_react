#\!/bin/bash
#https://phoenixnap.com/kb/debian-install-nodejs
yarn create vite .
yarn --exact
#yarn dev to run server
sudo sysctl fs.inotify.max_queued_events=16384
sudo sysctl fs.inotify.max_user_instances=8192
sudo sysctl fs.inotify.max_user_watches=524288
#yarn dev --host
npx tailwindcss init -p
