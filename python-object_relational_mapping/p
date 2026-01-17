#!/bin/bash

# التحقق هل كتبت رسالة أم لا
if [ -z "$1" ]; then
    # إذا لم تكتب رسالة، سيضع رسالة افتراضية (استخدمها بحذر)
    msg="Update files"
else
    # إذا كتبت رسالة، سيستخدمها
    msg="$1"
fi

echo "Adding files..."
git add .

echo "Committing with message: $msg"
git commit -m "$msg"

echo "Pushing to GitHub..."
git push

echo "🚀 Done!"
