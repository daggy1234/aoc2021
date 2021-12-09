if ! hash "ghc"; then
    echo "ghc not found"
    exit 1
fi

for file in *; do
    if [ -d "$file" ] && [[ $file == day* ]]; then
        echo "========================================="
        if [ -f "$file/day${file:3}.hs" ]; then
            echo "Compiling Day ${file:3}"
            eval "cd $file && ghc day${file:3}.hs -O2 && ./day${file:3} && cd .."
        else
            echo "No Haskell Solution for Day ${file:3}"
        fi
    fi
done