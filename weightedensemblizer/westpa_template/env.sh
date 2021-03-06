# This file defines where WEST and GROMACS can be found
# Modify to taste

# Inform WEST where to find Python and our other scripts where to find WEST
export WEST_PYTHON=template_west_python
export WEST_ROOT=template_west_root

# Explicitly name our simulation root directory
if [[ -z "$WEST_SIM_ROOT" ]]; then
    export WEST_SIM_ROOT="$PWD"
fi
export SIM_NAME=$(basename "$WEST_SIM_ROOT")
echo "simulation $SIM_NAME root is $WEST_SIM_ROOT"
