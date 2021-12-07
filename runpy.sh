if ! hash "python3"; then
    if ! hash "python"; then
        echo "python is not installed"
        exit 1
    else
        PYNAME="python"
        echo "python3 not found, using python"
    fi
else
    PYNAME="python3"
    echo "Using python3"
fi

ver=$($PYNAME -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')

if [ "$ver" -lt "38" ]; then
    echo "This script requires python 3.8 or greater. $PYNAME has version $ver"
    exit 1
fi

echo "Running stuff"
exec $PYNAME runner.py
echo "All done"
