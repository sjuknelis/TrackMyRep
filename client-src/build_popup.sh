#!/bin/bash
cp vue_popup.config.js vue.config.js &&
cp src/main_popup.js src/main.js &&
npm run build &&
rm -rf ../client/popup &&
mv dist ../client/popup &&
rm vue.config.js &&
rm src/main.js