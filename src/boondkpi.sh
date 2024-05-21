#!/bin/sh -x

locate_python() {
  for c in python3.9 python3.8 python3; do
    p=$(which $c)
    if [ $? -ne 0 ]; then continue; fi
    PYTHON_CMD=$(basename $p)
    return 0
  done
  echo "python3 must be in PATH"
  exit -1
}

start() {
  if [ -f $BOONDKPI_REPO/$VENV/bin/activate ]; then
    . $BOONDKPI_REPO/$VENV/bin/activate
  else
    echo "you must setup first"
    exit -1
  fi
  cd $BOONDKPI_REPO
  $PYTHON_CMD boondkpi.py  $*
}

setup() {
  $PYTHON_CMD -m venv $BOONDKPI_REPO/$VENV
  . $BOONDKPI_REPO/$VENV/bin/activate
  $PYTHON_CMD -m pip install --upgrade pip
  $PYTHON_CMD -m pip install --no-cache-dir -r requirements.txt
}

# main
BOONDKPI_REPO=$(dirname $0)
VENV=hapenv

case "$1" in
setup)
  locate_python
  setup
  ;;
start)
  locate_python
  shift
  start $*
  ;;
*)
  echo "Usage: $0 {start|setup}"
  ;;
esac
exit 0
