import re                                                  

def check_strength(password):                             
    score = 0                                              
    feedback = []                                          

    if len(password) >= 12:                                
        score += 2                                         
    elif len(password) >= 8:                               
        score += 1                                         
    else:                                                  
        feedback.append("Use at least 12 characters.")    

    checks = [                                             
        (r"[a-z]", "Add lowercase letters."),              
        (r"[A-Z]", "Add uppercase letters."),              
        (r"[0-9]", "Add numbers."),                        
        (r"[^a-zA-Z0-9]", "Add symbols like ! @ #."),      
    ]                                                      
    for pattern, tip in checks:                            
        if re.search(pattern, password):                   
            score += 1                                     
        else:                                              
            feedback.append(tip)                           

    if score >= 6:                                         
        rating = "Strong"                                  
    elif score >= 4:                                       
        rating = "Medium"                                  
    else:                                                  
        rating = "Weak"                                    
    return rating, score, feedback                         

if __name__ == "__main__":                                 
    pw = input("Enter a password: ")                       
    rating, score, feedback = check_strength(pw)          
    print(f"Strength: {rating} ({score}/6)")               
    for tip in feedback:                                   
        print(" -", tip)                                  