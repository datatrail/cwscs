def get_summary_lots(lots):
    print("")
    print("-------------------------------------------------")
    print("All lots")
    print("-------------------------------------------------")
    total = 0
    for lot in lots:
        total += lot.current_bid_amount
        print(lot.id, lot.current_bid_amount, lot.title)
    print("-------------------------------------------------")
    print(f"Total: {total} (nr of lots: {len(lots)}, avg: {round(total / len(lots),2)})")


def get_summary_closed_lots(lots):
    print("")
    print("-------------------------------------------------")
    print("Closed lots")
    print("-------------------------------------------------")
    total = 0
    lot_count = 0
    for lot in lots:
        if lot.closed:
            total += lot.current_bid_amount
            lot_count += 1
            print(lot.id, lot.current_bid_amount, lot.title)
    print("-------------------------------------------------")
    print(f"Total: {total} (nr of lots: {lot_count}, avg: {round(total / lot_count, 2)})")


def get_summary_open_lots(lots):
    print("")
    print("-------------------------------------------------")
    print("Open lots")
    print("-------------------------------------------------")
    total = 0
    lot_count = 0
    for lot in lots:
        if not lot.closed:
            total += lot.current_bid_amount
            lot_count += 1
            print(lot.id, lot.current_bid_amount, lot.title)
    print("-------------------------------------------------")
    print(f"Total: {total} (nr of lots: {lot_count}, avg: {round(total / lot_count, 2)})")
