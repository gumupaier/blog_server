#!/usr/bin/env bash

cd /work
#pip install -r requirements.txt -i https://pypi.douban.com/simple

if [ "$DEBUG" == "true" ]; then
    echo "use debug mode"
    python setup.py develop
else
    echo "use product mode"
	python setup.py install

fi

flask forge
exec "$@"
