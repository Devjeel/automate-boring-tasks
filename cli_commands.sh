#!/bin/bash

function shutdown {
    python -c 'import script; script.shutdown()'
}

function restart {
    python -c 'import script; script.restart()'
}

function logout {
    python -c 'import script; script.logout()'
}