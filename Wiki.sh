#!/bin/bash
base_url="http://en.wikipedia.org/wiki/"
$link
link="${link//" "/"_"}"
google-chrome $base_url$link