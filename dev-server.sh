#!/bin/sh

set -e

die() {
    echo "[31m$*[0m"
    exit 1
}

test -e manage.py || die 'Скрипт должен быть запущен в корне проекта (где лежит manage.py)'
which sass >/dev/null || die 'SASS не установлен. (https://sass-lang.com/install)'

# Прибить django и sass при выходе
trap 'kill $(jobs -p)' EXIT

source venv/bin/activate
./manage.py runserver &
sass --watch okaymoneyapp/sass:okaymoneyapp/static/okaymoneyapp/css &
while true; do
    true  # Бесконечный цикл
done
