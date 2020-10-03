#!/bin/bash

echo "Syncing Notes"
git pull

echo ""
echo "Staging Changed Files"
git add .

echo ""
echo "Committing Staged Files"
git commit -m "Sync Notes -$(date)"

echo ""
echo "Pushing changes to GitHub"
git push

echo ""
echo "Finished Syncing"