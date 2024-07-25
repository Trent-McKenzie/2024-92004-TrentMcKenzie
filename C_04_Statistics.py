# Statistics Area #

if rounds_played > 0:
    # Calculate Statistics
    percent_won = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100

    # Output Game Statistics
    print("📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Won: {percent_won:.2f} \t "
          f"😥 Lost: {percent_lost:.2f} \t ")

    # ask user if they want to see their game history and output it if requested.
    see_history = string_checker("\nDo you want to see your game history? ", yes_no)
    if see_history == "yes":
        for item in game_history:
            print(item)
