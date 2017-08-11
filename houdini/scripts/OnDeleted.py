"""Perform tasks when a Houdini node is deleted."""

# =============================================================================
# IMPORTS
# =============================================================================

# Houdini Toolbox Imports
from ht.events import NodeEvents, runEvent

# =============================================================================
# FUNCTIONS
# =============================================================================

def main():
    """Main function."""
    runEvent(NodeEvents.OnDeleted, kwargs)

# =============================================================================

main()

