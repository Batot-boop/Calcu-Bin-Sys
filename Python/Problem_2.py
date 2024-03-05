
# >>>>>>>>> Main Function <<<<<<<<< #

def main():
    
    # >>>>>>>>> Start Program <<<<<<<<< #
    
    while True:
         
    # >>>>>>>>> menu_1 that is displayed to the user <<<<<<<<< #
        
        menu_1()
        
    # >>>>>>>>> Check valid choice <<<<<<<<< #    
        
        while True:
            letter_of_start_or_exit = input("Please select our choice (A/B): ").upper()
            if letter_of_start_or_exit == 'A' or letter_of_start_or_exit == 'B':
                break
            else:
                print("Please select a valid choice.")
        
    # >>>>>>>>> Check that input number is binary or not and Check ValueError <<<<<<<<< #  
      
        if letter_of_start_or_exit == 'A':
            while True:
                try:
                    num_of_insert = input("Please insert number is a valid binary number: ")
                    int(num_of_insert,2)
                    break
                except ValueError:
                    print("Please insert a valid binary number.")
            
        # >>>>>>>>> menu_2 that is displayed to the user <<<<<<<<< #    
            
            menu_2()
            
        # >>>>>>>>> Check valid choice <<<<<<<<< #    
            
            while True:
                letter_of_compute = input("Please select your choice (A/B/C/D): ").upper()
                if letter_of_compute == 'A' or letter_of_compute == 'B' or letter_of_compute == 'C' or letter_of_compute == 'D':
                    break
                else:
                    print("Please select a valid choice.")
            
        # >>>>>>>>> Conditions for choosing arithmetic operations <<<<<<<<< #    
            
            if letter_of_compute == 'A':
                compute_ones_complement(num_of_insert)
            elif letter_of_compute == 'B':
                compute_twos_complement(num_of_insert)
            elif letter_of_compute == 'C':
                addition(num_of_insert)
            elif letter_of_compute == 'D':
                subtraction(num_of_insert) 
             
    # >>>>>>>>> End program <<<<<<<<< #
        
        elif letter_of_start_or_exit == 'B':
            print("\nExiting program\n")
            break

                        #=========================================== Start Menus Functions ===========================================#    

# >>>>>>>>> Menu_1 Function <<<<<<<<< #

def menu_1():
    print("\n\n ** Binary Calculator ** \n")
    print("A) Insert new number\n")
    print("B) Exit\n")
    
# >>>>>>>>> Menu_2 Function <<<<<<<<< #

def menu_2():
    print("\n\n ** Please select the operation ** \n")
    print("A) Compute one's complement\n")
    print("B) Compute two's complement\n")
    print("C) Addition\n")
    print("D) Subtraction\n")

                        #=========================================== Start Computing Functions ===========================================#
    
# >>>>>>>>> Compute_One's_Complement Function <<<<<<<<< #

def compute_ones_complement(number_of_insert):
    binary_num = number_of_insert
    ones_comp = ''
    for bit in binary_num:
        ones_comp += '0' if bit == '1' else '1'
    print(f"Result:  {ones_comp}") 

# >>>>>>>>> Compute_Two's_Complement Function <<<<<<<<< #

def compute_twos_complement(number_of_insert):
    binary_num = number_of_insert
    ones_comp = ''
    for bit in binary_num:
        ones_comp += '0' if bit == '1' else '1'
    ones_comp_int = int(ones_comp, 2)
    twos_comp_int = ones_comp_int + 1
    twos_comp = ''
    while twos_comp_int > 0:
        twos_comp = str(twos_comp_int % 2) + twos_comp
        twos_comp_int //= 2
    print(f"Result:  {twos_comp}")

# >>>>>>>>> Compute_Addition Function <<<<<<<<< #

def addition(number_of_insert):
    num1 = number_of_insert
    while True:
        try:
            num2 = input("Please insert the second number: ")
            int(num2,2)
            break
        except ValueError:
            print("Please insert a valid binary number.")
    result = ''
    carry = 0
    i, j = len(num1) - 1, len(num2) - 1
    while i >= 0 or j >= 0:
        sum_ = carry
        if i >= 0:
            sum_ += int(num1[i])
            i -= 1
        if j >= 0:
            sum_ += int(num2[j])
            j -= 1
        result += str(sum_ % 2)
        carry = sum_ // 2
    if carry:
        result += str(carry)
        print(f"Result:  {result[::-1]}") 

# >>>>>>>>> Compute_Subtraction Function<<<<<<<<< #

def subtraction(number_of_insert):
    num1 = number_of_insert
    while True:
        try:
            num2 = input("Please insert the second number: ")
            int(num2,2)
            break
        except ValueError:
            print("Please insert a valid binary number.")
    
    result = ''
    borrow = 0
    i, j = len(num1) - 1, len(num2) - 1
    while i >= 0 or j >= 0:
        diff = borrow
        if i >= 0:
            diff += int(num1[i])
            i -= 1
        if j >= 0:
            diff -= int(num2[j])
            j -= 1
        result += str(diff % 2)
        borrow = diff // 2
    if borrow:
        result += str(borrow)
    print(f"Result:  {result[::-1]}") 


main()


#Student name(1): Islam Ahmed Salah ID(1): 20230056      
#Student name(2): Islam Hassan Jalbee ID(2): 20230059
#Student name(3): Ahmed Hassan Abdel Hamed ID(3): 20230014