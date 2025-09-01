class MainMenu:
    def __init__(self,
                 players_manager):
        self.players_manager = players_manager

    def show_menu(self):
        """Display the main menu and handle user input."""
        while True:
            print("\n=== Main Menu ===")
            print("1. List the players")
            print("2. Add a player")
            print("3. List the tournaments")
            print("4. Add a tournament")
            print("5. Register players to a tournament")
            print("6. Start tournament")
            print("7. Start a round")
            print("8. Enter round results")
            print("0. Exit")

            choice = input("Select an option: ").strip()
            self.handle_choice(choice)

    def handle_choice(self, choice: str):
        """Route user choice to the correct controller action."""
        if choice == "1":
            self.players_manager.list_players()
        elif choice == "2":
            self.players_manager.add_player()
#        elif choice == "3":
#            self.tournaments_controller.add_tournament()
#        elif choice == "4":
#            self.tournaments_controller.add_tournament()
#        elif choice == "5":
#            self.tournaments_controller.register_players()
#        elif choice == "6":
#            self.tournaments_controller.start_tournament()
#        elif choice == "7":
#            self.rounds_controller.start_round()
#        elif choice == "8":
#            self.rounds_controller.enter_results()

        elif choice == "0":
            print("Exiting...")
            exit(0)
        else:
            print("Invalid choice. Try again.")
