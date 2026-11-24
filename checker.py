import re                                                  # 0

def check_strength(password):                              # 0
    score = 0                                              # 1 Tab
    feedback = []                                          # 1 Tab

    if len(password) >= 12:                                # 1 Tab
        score += 2                                         # 2 Tabs
    elif len(password) >= 8:                               # 1 Tab
        score += 1                                         # 2 Tabs
    else:                                                  # 1 Tab
        feedback.append("Use at least 12 characters.")    # 2 Tabs

    checks = [                                             # 1 Tab
        (r"[a-z]", "Add lowercase letters."),              # 2 Tabs
        (r"[A-Z]", "Add uppercase letters."),              # 2 Tabs
        (r"[0-9]", "Add numbers."),                        # 2 Tabs
        (r"[^a-zA-Z0-9]", "Add symbols like ! @ #."),      # 2 Tabs
    ]                                                      # 1 Tab
    for pattern, tip in checks:                            # 1 Tab
        if re.search(pattern, password):                   # 2 Tabs
            score += 1                                     # 3 Tabs
        else:                                              # 2 Tabs
            feedback.append(tip)                           # 3 Tabs

    if score >= 6:                                         # 1 Tab
        rating = "Strong"                                  # 2 Tabs
    elif score >= 4:                                       # 1 Tab
        rating = "Medium"                                  # 2 Tabs
    else:                                                  # 1 Tab
        rating = "Weak"                                    # 2 Tabs
    return rating, score, feedback                         # 1 Tab

if __name__ == "__main__":                                 # 0
    pw = input("Enter a password: ")                       # 1 Tab
    rating, score, feedback = check_strength(pw)           # 1 Tab
    print(f"Strength: {rating} ({score}/6)")               # 1 Tab
    for tip in feedback:                                   # 1 Tab
        print(" -", tip)                                   # 2 Tabs