#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🔍 Regenerating search index..."
python3 "$SCRIPT_DIR/scripts/generate_search_index.py"

echo "✅ Build complete!"
echo ""
echo "To test locally, run:"
echo "  python3 -m http.server 8000"
echo ""
echo "Then visit: http://localhost:8000/notes/"
