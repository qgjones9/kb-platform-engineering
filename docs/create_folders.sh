# create a new folder and index.md file based on the first argument
# usage: ./create_folders.sh "Page Name" [target_directory]

# Check if page name argument is provided
if [ -z "$1" ]; then
    echo "Error: Page name is required"
    echo "Usage: $0 \"Page Name\" [target_directory]"
    exit 1
fi

# Set target directory (use second argument if provided, otherwise use current directory)
TARGET_DIR="${2:-.}"

# Create target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Convert to absolute path
if [ -d "$TARGET_DIR" ]; then
    TARGET_DIR=$(cd "$TARGET_DIR" && pwd)
else
    echo "Error: Cannot create or access target directory: $TARGET_DIR"
    exit 1
fi

echo "Target directory: $TARGET_DIR"

# Get page name from first argument
PAGE_NAME="$1"

# strip trailing whitespace, carriage returns, and remove brackets
PAGE_NAME=$(echo "$PAGE_NAME" | sed 's/[[:space:]]*$//' | tr -d '\r\n' | sed 's/\[//g' | sed 's/\]//g')

# skip if page name is empty after processing
if [ -z "$PAGE_NAME" ]; then
    echo "Error: Page name is empty after processing"
    exit 1
fi

# store original name for page title
ORIGINAL_NAME="$PAGE_NAME"

# convert folder name to lowercase
FOLDER_NAME=$(echo "$PAGE_NAME" | tr '[:upper:]' '[:lower:]')

# convert spaces into hyphens
FOLDER_NAME=$(echo "$FOLDER_NAME" | tr ' ' '-')

# remove brackets and other problematic characters from folder name
FOLDER_NAME=$(echo "$FOLDER_NAME" | sed 's/\[//g' | sed 's/\]//g' | sed 's/[^a-z0-9-]//g')

# skip if folder name is empty after processing
if [ -z "$FOLDER_NAME" ]; then
    echo "Error: Folder name is empty after processing"
    exit 1
fi

# Create folder in target directory
FULL_FOLDER_PATH="$TARGET_DIR/$FOLDER_NAME"
mkdir -p "$FULL_FOLDER_PATH"
echo "Folder $FULL_FOLDER_PATH created"

echo "Creating index.md file"
touch "$FULL_FOLDER_PATH/index.md"

echo "Adding content to index.md file"
echo "## $ORIGINAL_NAME" > "$FULL_FOLDER_PATH/index.md"

echo "Successfully created folder and index.md for: $ORIGINAL_NAME"

