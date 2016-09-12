#RELEASE_VERSION=1.0.0
#DEBUGBUILD=true
echo debugbuild=$DEBUGBUILD
if $DEBUGBUILD ;then
    echo "true"
else
    echo "false"
fi

if [[ -z "$RELEASE_VERSION" && -n "$DEBUGBUILD" ]] && $DEBUGBUILD ;then
    echo "true"
else
    echo "false"
fi
