#!/usr/bin/env bash

echo "Starting up Self-help Programs API"


cat << "EOF"

        .        .       .
,-. ,-. |  ,"    |-. ,-. |  ,-.    ,-. ,-. ,-. ,-. ,-. ,-. ,-,-. ,-.
`-. |-' |  |- -- | | |-' |  | | -- | | |   | | | | |   ,-| | | | `-.
`-' `-' `' |     ' ' `-' `' |-'    |-' '   `-' `-| '   `-^ ' ' ' `-'
           '                |      |            ,|
                            '      '            `'

EOF

cat << "EOF"

  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \_
__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/
  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \_
__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/
  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \_
__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/
  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \__/  \_


EOF


docker-compose up -d
echo "Seeding DB"
docker-compose run --rm api python manage.py create_fixtures
echo "Seeded DB"
echo "API ready at http://0.0.0.0:5000/graphql"
