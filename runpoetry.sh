if ! hash "poetry"; then
        exit 1
fi

echo "Running with poetry"
eval poetry run python runner.py "python"
echo "All done"
