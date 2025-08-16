"""Point d'entrée."""

# Initialize app (create data directory if needed)
from controllers import init_app

# Import controller to manage players
from controllers.manage_players import AddPlayer

# Optional: here you could trigger CLI or other operations
