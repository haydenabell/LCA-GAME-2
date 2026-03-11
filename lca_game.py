import sys

def print_divider():
    print("\n" + "="*60 + "\n")

def game():
    score = 0
    print_divider()
    print("WELCOME, LCA MANAGER!")
    print("Your mission: Navigate the life cycle of a new office building.")
    print("Balance carbon footprints, costs, and circularity to win.")
    print_divider()

    # --- STAGE A1-A3: Product Stage ---
    print("STAGE 1: Product Stage (A1–A3)")
    print("You need to select the primary structural material.")
    print("1) Standard Portland Cement Concrete (High embodied carbon)")
    print("2) Cross-Laminated Timber (CLT) (Carbon sequestration, but higher cost)")
    
    choice1 = input("Choose 1 or 2: ")
    if choice1 == "2":
        score += 50
        print("\nFEEDBACK: Great choice! Using timber reduces the A1-A3 footprint significantly.")
    else:
        score += 10
        print("\nFEEDBACK: Conventional choice. High initial carbon emissions recorded.")

    # --- STAGE A4-A5: Construction Stage ---
    print_divider()
    print("STAGE 2: Construction Process (A4–A5)")
    print("Logistics time! How will you get materials to the site?")
    print("1) Source locally (50km) but with slightly lower grade specs.")
    print("2) Import high-spec materials from overseas (8,000km via shipping).")

    choice2 = input("Choose 1 or 2: ")
    if choice2 == "1":
        score += 40
        print("\nFEEDBACK: Low transport emissions (A4) boosted your score!")
    else:
        score -= 20
        print("\nFEEDBACK: Shipping emissions and port logistics added a heavy carbon debt.")

    # --- STAGE B1-B7: Use Stage ---
    print_divider()
    print("STAGE 3: Use Stage (B1–B7)")
    print("The building is live. How do you handle maintenance and energy?")
    print("1) Install smart sensors and a high-efficiency HVAC system.")
    print("2) Use a standard system to save on upfront construction costs.")

    choice3 = input("Choose 1 or 2: ")
    if choice3 == "1":
        score += 60
        print("\nFEEDBACK: Massive B6 (Operational Energy) savings over the 50-year lifespan!")
    else:
        score -= 30
        print("\nFEEDBACK: The 'cheap' system is leaking energy and carbon daily. Poor B-stage performance.")

    # --- STAGE C1-C4 & D: End-of-Life & Beyond ---
    print_divider()
    print("STAGE 4: End-of-Life & Benefits (C & D)")
    print("50 years have passed. The building is being decommissioned.")
    print("1) Demolish and send to landfill (C4).")
    print("2) Design for Disassembly: Modular parts are recovered for reuse (Stage D).")

    choice4 = input("Choose 1 or 2: ")
    if choice4 == "2":
        score += 100
        print("\nFEEDBACK: You've achieved Circularity! Stage D credits applied for future reuse.")
    else:
        score -= 50
        print("\nFEEDBACK: High waste impact. You missed the chance to offset your A1 emissions.")

    # --- FINAL SCORE ---
    print_divider()
    print(f"FINAL LCA SCORE: {score} POINTS")
    
    if score >= 200:
        print("RANK: SUSTAINABILITY CHAMPION 🌿")
    elif score >= 100:
        print("RANK: COMPLIANT MANAGER 🏗️")
    else:
        print("RANK: CARBON OFFENDER ⚠️")
    print_divider()

if __name__ == "__main__":
    game()
