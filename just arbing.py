def arbitrage_calculator():
    print("=== Arbitrage Calculator (KES) ===\n")

    try:
        total_stake = float(input("Enter total stake (KES): "))
        if total_stake <= 0:
            raise ValueError
    except ValueError:
        print("Invalid stake amount.")
        return

    bets = []

    print("\nEnter outcomes (minimum 2). Leave outcome empty to stop.\n")

    while True:
        outcome = input("Outcome name (or press Enter to finish): ").strip()
        if outcome == "":
            break

        try:
            odds = float(input("  Odds: "))
            tax = float(input("  Tax % (0 if none): "))
            if odds <= 1:
                print("  Odds must be greater than 1.\n")
                continue
        except ValueError:
            print("  Invalid input.\n")
            continue

        bets.append({
            "outcome": outcome,
            "odds": odds,
            "tax": tax
        })
        print()

    if len(bets) < 2:
        print("You must enter at least 2 valid outcomes.")
        return

    # Calculate implied probability sum
    implied_sum = sum(1 / bet["odds"] for bet in bets)

    if implied_sum >= 1:
        print("\n❌ No arbitrage opportunity.")
        return

    print("\n✅ Arbitrage Opportunity Found!\n")
    print("Results:")
    print("-" * 50)

    net_payouts = []

    for bet in bets:
        stake = (total_stake / bet["odds"]) / implied_sum
        gross = stake * bet["odds"]
        net = gross * (1 - bet["tax"] / 100)

        net_payouts.append(net)

        print(
            f"{bet['outcome']} → "
            f"Stake: KES {stake:.2f}, "
            f"Net Payout: KES {net:.2f}"
        )

    guaranteed = min(net_payouts)
    profit = guaranteed - total_stake
    roi = (profit / total_stake) * 100

    print("-" * 50)
    print(f"Guaranteed Payout: KES {guaranteed:.2f}")
    print(f"Profit: KES {profit:.2f} ({roi:.2f}%)")


if __name__ == "__main__":
    arbitrage_calculator()
