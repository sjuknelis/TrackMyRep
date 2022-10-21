#!/bin/bash
cp vue_popout.config.js vue.config.js &&
cp src/main_popout.js src/main.js &&
npm run build &&
rm -rf ../client/popout &&
mv dist ../client/popout &&
rm vue.config.js &&
rm src/main.js