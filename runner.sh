if ! hash python3; then
    echo "python3 is not installed"
    exit 1
fi

ver=$(python3 -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')

if [ "$ver" -lt "38" ]; then
    echo "This script requires python 3.8 or greater"
    exit 1
fi

if ! hash cargo; then
    echo "cargo is not installed"
    exit 1
fi
echo "Running stuff"
exec python3 runner.py
echo "All done"
