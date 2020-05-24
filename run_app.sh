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


docker-compose up


echo "FlASK_APP PATH: ${FLASK_APP}"
echo "POSTGRES PORT: ${POSTGRES_PORT}"