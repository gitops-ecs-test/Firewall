#!/bin/bash

# Go to the repository
cd /home/ubuntu/Firewall || exit 1

# Run the backup
python3 scripts/backup.py

# Stage only the backups directory
git add backups/

# Commit only if there are changes
if ! git diff --cached --quiet; then
    git commit -m "Automated backup $(date '+%Y-%m-%d %H:%M:%S')"
    git push origin backups
fi
