print("welcome to the fist problem set of the Algorithms II series.")
print("write the number of the problem that u want to test and it gonna be started.")
print("the problem set contains 24 problem soo chose from 1 to 24.")



problem = int(input("enter the number of the problem u wanna try : "))

if problem == 1 : 
    # Read three integers from input             
    a = int(input("Enter the first integer: "))  
    b = int(input("Enter the second integer: ")) 
    c = int(input("Enter the third integer: "))  
                                             
    # Find maximum                               
    max_val = a                                  
    if b > max_val:                              
        max_val = b                              
    if c > max_val:                              
        max_val = c                              
                                             
    # Find minimum                               
    min_val = a                                  
    if b < min_val:                              
        min_val = b                              
    if c < min_val:                              
        min_val = c                              
                                             
    # Output results                             
    print(f"Maximum: {max_val}")                 
    print(f"Minimum: {min_val}")                 
elif problem == 2 :
    print("here there is only the correction of the first question if u want the others implement them urslf body :).") 

    x = flout(input("enter ur real number : "))
    n = int(input("enter the natural number : "))
    def power(x, n):       
        return X**n
    result = 1                             
    for _ in range(n):                     
        result *= x                            
        return result                          
                                           
    x = float(input("Enter base (x): "))   
    n = int(input("Enter exponent (n): ")) 
    print(f"{x}^{n} = {power(x, n)}")      
elif problem == 3 :      
    print("here there is only the correction of the first question if u want the others implement them urslf body :).")   
    
    def calculate_product_A(N):                           
        product = 1                                       
        for k in range(2, N + 1):                         
            sum_k = k * (k + 1) // 2  # Triangular number 
            product *= sum_k                              
        return product                                    
                                                          
    N = int(input("Enter N (≥ 2): "))                     
    if N < 2:                                             
        print("Error: N must be ≥ 2")                     
    else:                                                 
        print(f"Product A = {calculate_product_A(N)}")    
elif problem == 4 :      
    def find_divisors(n):                                
        n_abs = abs(n)                                   
        divisors = []                                    
        for i in range(1, n_abs + 1):                    
            if n_abs % i == 0:                           
                divisors.append(i)                       
        return divisors                                  
                                                         
    try:                                                 
        N = int(input("Enter an integer: "))             
        result = find_divisors(N)                        
        print(f"Divisors of {N}: {result}")              
    except ValueError:                                   
        print("Invalid input. Please enter an integer.") 
elif problem == 5 :      
    import math                                                          
                                                                         
    def is_prime(n):                                                     
        if n <= 1:                                                       
            return False                                                 
        if n == 2:                                                       
            return True                                                  
        if n % 2 == 0:                                                   
            return False                                                 
        for i in range(3, math.isqrt(n) + 1, 2):                         
            if n % i == 0:                                               
                return False                                             
        return True                                                      
                                                                         
    try:                                                                 
        N = int(input("Enter a positive integer: "))                     
        if is_prime(N):                                                  
            print(f"{N} is a prime number.")                             
        else:                                                            
            print(f"{N} is not a prime number.")                         
    except ValueError:                                                   
        print("Invalid input. Please enter an integer.")                 
elif problem == 6 :      
    def sum_odd_numbers(N, M):                                     
        if N >= M:                                                 
            return "Error: N must be less than M"                  
        total = 0                                                  
        for num in range(N, M + 1):                                
            if num % 2 == 1:                                       
                total += num                                       
        return total                                               
                                                                   
    try:                                                           
        N = int(input("Enter N (1 ≤ N < M): "))                    
        M = int(input("Enter M (M > N): "))                        
        result = sum_odd_numbers(N, M)                             
        print(f"Sum of odd numbers between {N} and {M}: {result}") 
    except ValueError:                                             
        print("Invalid input. Please enter integers.")             
elif problem == 7 :      
    def is_right_triangle():                                         
        try:                                                         
            a = int(input("Enter side a: "))                         
            b = int(input("Enter side b: "))                         
            c = int(input("Enter side c: "))                         
        except ValueError:                                           
            print("Invalid input: All sides must be integers.")      
            return                                                   
                                                                     
        if a <= 0 or b <= 0 or c <= 0:                               
            print("All sides must be positive integers.")            
            return                                                   
                                                                     
        sides = sorted([a, b, c])                                    
        a, b, c = sides                                              
                                                                     
        if a + b <= c:                                               
            print("Invalid triangle: Triangle inequality violated.") 
            return                                                   
                                                                     
        if a**2 + b**2 == c**2:                                      
            print("This is a right-angled triangle.")                
        else:                                                        
            print("This is not a right-angled triangle.")            
                                                                     
    is_right_triangle()                                              
elif problem == 8 :      
    def binary_to_decimal():                                         
        try:                                                         
            N = int(input("Enter the number of bits: "))             
            if N <= 0:                                               
                print("Number of bits must be positive.")            
                return                                               
        except ValueError:                                           
            print("Invalid input. Please enter an integer.")         
            return                                                   
                                                                     
        decimal = 0                                                  
        for i in range(N):                                           
            while True:                                              
                bit = input(f"Enter bit number {N - 1 - i}: ")       
                if bit in ['0', '1']:                                
                    decimal = decimal * 2 + int(bit)                 
                    break                                            
                else:                                                
                    print("Invalid input. Please enter '0' or '1'.") 
                                                                     
        print(f"The decimal value is: {decimal}")                    
                                                                     
    binary_to_decimal()                                              
elif problem == 9 :      
    def compute_sequence_term(n):                                  
        if n < 0:                                                  
            return "Error: n must be a non-negative integer."      
        if n == 0:                                                 
            return 2.0                                             
        if n == 1:                                                 
            return 3.0                                             
                                                                   
        u0, u1 = 2.0, 3.0                                          
        for _ in range(2, n + 1):                                  
            u2 = (2/3) * u1 - (1/4) * u0                           
            u0, u1 = u1, u2                                        
        return u2                                                  
                                                                   
    try:                                                           
        n = int(input("Enter a non-negative integer n: "))         
        result = compute_sequence_term(n)                          
        print(f"The {n}-th term of the sequence is: {result:.6f}") 
    except ValueError:                                             
        print("Invalid input. Please enter an integer.")           
elif problem == 10 :      
    def collatz_steps():                                       
        try:                                                   
            u0 = int(input("Enter a positive integer (u0): ")) 
            if u0 <= 0:                                        
                print("Error: u0 must be a positive integer.") 
                return                                         
        except ValueError:                                     
            print("Invalid input. Please enter an integer.")   
            return                                             
                                                               
        n = 0                                                  
        current = u0                                           
        while current != 1:                                    
            if current % 2 == 0:                               
                current = current // 2                         
            else:                                              
                current = 3 * current + 1                      
            n += 1                                             
        print(f"The smallest n for which u_n = 1 is: {n}")     
                                                               
    collatz_steps()                                            
elif problem == 11 :      
    def compute_sequence_term():                                            
        try:                                                                
            a = float(input("Enter a strictly positive real number (a): ")) 
            if a <= 0:                                                      
                print("Error: a must be a positive real number.")           
                return                                                      
        except ValueError:                                                  
            print("Invalid input. Please enter a valid real number.")       
            return                                                          
                                                                            
        epsilon = 1e-6                                                      
        U_prev = a                                                          
        n = 0                                                               
                                                                            
        while True:                                                         
            U_curr = 1 + U_prev / (1 + 2 * U_prev)                          
            diff = abs(U_curr - U_prev)                                     
            U_prev = U_curr                                                 
            n += 1                                                          
            if diff < epsilon:                                              
                break                                                       
                                                                            
        print(f"Converged to U_n = {U_curr:.10f} after {n} iterations.")    
                                                                            
    compute_sequence_term()                                                 
elif problem == 12 :      
    def newton_raphson_sqrt():                                                          
        try:                                                                            
            A = float(input("Enter a strictly positive real number (A): "))             
            if A <= 0:                                                                  
                print("Error: A must be strictly positive.")                            
                return                                                                  
        except ValueError:                                                              
            print("Invalid input. Please enter a valid real number.")                   
            return                                                                      
                                                                                        
        epsilon = 1e-9                                                                  
        X_prev = A                                                                      
        iterations = 0                                                                  
                                                                                        
        while True:                                                                     
            X_curr = 0.5 * (X_prev + A / X_prev)                                        
            diff = abs(X_curr - X_prev)                                                 
            X_prev = X_curr                                                             
            iterations += 1                                                             
            if diff < epsilon:                                                          
                break                                                                   
                                                                                        
        print(f"Approximated sqrt({A}) = {X_curr:.10f} after {iterations} iterations.") 
                                                                                        
    newton_raphson_sqrt()                                                               
elif problem == 13 :      
    def array_operations():                                                    
        try:                                                                   
            N = int(input("Enter the size of the array (positive integer): ")) 
            if N <= 0:                                                         
                print("Error: Array size must be positive.")                   
                return                                                         
        except ValueError:                                                     
            print("Invalid input. Please enter an integer.")                   
            return                                                             
                                                                               
        T = []                                                                 
        print(f"Enter {N} integers:")                                          
        for i in range(N):                                                     
            while True:                                                        
                try:                                                           
                    x = int(input(f"Element {i + 1}: "))                       
                    T.append(x)                                                
                    break                                                      
                except ValueError:                                             
                    print("Invalid input. Please enter an integer.")           
                                                                               
        print("Array:", T)                                                     
        total = sum(T)                                                         
        print("Sum of elements:", total)                                       
                                                                               
    array_operations()                                                         
elif problem == 14 :      
    def array_separation():                                                                
        try:                                                                               
            N = int(input("Enter the size of the array (positive integer): "))             
            if N <= 0:                                                                     
                print("Error: Array size must be positive.")                               
                return                                                                     
        except ValueError:                                                                 
            print("Invalid input. Please enter an integer.")                               
            return                                                                         
                                                                                           
        T = []                                                                             
        print(f"Enter {N} integers:")                                                      
        for i in range(N):                                                                 
            while True:                                                                    
                try:                                                                       
                    x = int(input(f"Element {i + 1}: "))                                   
                    T.append(x)                                                            
                    break                                                                  
                except ValueError:                                                         
                    print("Invalid input. Please enter an integer.")                       
                                                                                           
        T_POS = []                                                                         
        T_NEG = []                                                                         
        for x in T:                                                                        
            if x > 0:                                                                      
                T_POS.append(x)                                                            
            elif x < 0:                                                                    
                T_NEG.append(x)                                                            
                                                                                           
        print("Original array:", T)                                                        
        print("Positive elements:", T_POS)                                                 
        print("Negative elements:", T_NEG)                                                 
                                                                                           
    array_separation()                                                                     
elif problem == 15 :      
    import math                                                                
                                                                               
    def vector_norm():                                                         
        try:                                                                   
            N = int(input("Enter the size of the array (positive integer): ")) 
            if N <= 0:                                                         
                print("Error: Array size must be positive.")                   
                return                                                         
        except ValueError:                                                     
            print("Invalid input. Please enter an integer.")                   
            return                                                             
                                                                               
        T = []                                                                 
        print(f"Enter {N} real numbers:")                                      
        for i in range(N):                                                     
            while True:                                                        
                try:                                                           
                    x = float(input(f"Element {i + 1}: "))                     
                    T.append(x)                                                
                    break                                                      
                except ValueError:                                             
                    print("Invalid input. Please enter a valid real number.")  
                                                                               
        sum_squares = sum(x**2 for x in T)                                     
        norm = math.sqrt(sum_squares)                                          
        print(f"The norm of the vector is: {norm:.6f}")                        
                                                                               
    vector_norm()                                                              
elif problem == 16 :      
   def vector_operations():                                                                    
       try:                                                                                    
           N = int(input("Enter the size of the vectors (positive integer): "))                
           if N <= 0:                                                                          
               print("Error: Vector size must be positive.")                                   
               return                                                                          
       except ValueError:                                                                      
           print("Invalid input. Please enter an integer.")                                    
           return                                                                              
                                                                                               
       v1 = []                                                                                 
       v2 = []                                                                                 
       print(f"Enter {N} real numbers for vector v1:")                                         
       for i in range(N):                                                                      
           while True:                                                                         
               try:                                                                            
                   x = float(input(f"Element {i + 1}: "))                                      
                   v1.append(x)                                                                
                   break                                                                       
               except ValueError:                                                              
                   print("Invalid input. Please enter a valid real number.")                   
                                                                                               
       print(f"Enter {N} real numbers for vector v2:")                                         
       for i in range(N):                                                                      
           while True:                                                                         
               try:                                                                            
                   y = float(input(f"Element {i + 1}: "))                                      
                   v2.append(y)                                                                
                   break                                                                       
               except ValueError:                                                              
                   print("Invalid input. Please enter a valid real number.")                   
                                                                                               
       sum_diff = 0.0                                                                          
       sum_dot = 0.0                                                                           
       for i in range(N):                                                                      
           diff = v1[i] - v2[i]                                                                
           sum_diff += diff * diff                                                             
           sum_dot += v1[i] * v2[i]                                                            
                                                                                               
       distance = sum_diff / (N * N)                                                           
       dot_product = sum_dot                                                                   
                                                                                               
       print(f"Distance between vectors: {distance:.6f}")                                      
       print(f"Dot product of vectors: {dot_product:.6f}")                                     
                                                                                               
   vector_operations()                                                                         
elif problem == 17 :      
    def reverse_array_in_place():                                               
        try:                                                                    
            N = int(input("Enter the size of the array (positive integer): "))  
            if N <= 0:                                                          
                print("Error: Array size must be positive.")                    
                return                                                          
        except ValueError:                                                      
            print("Invalid input. Please enter an integer.")                    
            return                                                              
                                                                                
        T = []                                                                  
        print(f"Enter {N} integers:")                                           
        for i in range(N):                                                      
            while True:                                                         
                try:                                                            
                    x = int(input(f"Element {i + 1}: "))                        
                    T.append(x)                                                 
                    break                                                       
                except ValueError:                                              
                    print("Invalid input. Please enter an integer.")            
                                                                                
        print("Original array:", T)                                             
                                                                                
        # In-place reversal                                                     
        i = 0                                                                   
        j = N - 1                                                               
        while i < j:                                                            
            T[i], T[j] = T[j], T[i]                                             
            i += 1                                                              
            j -= 1                                                              
                                                                                
        print("Reversed array:", T)                                             
                                                                                
    reverse_array_in_place()                                                    
elif problem == 18 :      
   def find_max_min_indices():                                                    
       try:                                                                       
           N = int(input("Enter the size of the array (positive integer): "))     
           if N <= 0:                                                             
               print("Error: Array size must be positive.")                       
               return                                                             
       except ValueError:                                                         
           print("Invalid input. Please enter an integer.")                       
           return                                                                 
                                                                                  
       T = []                                                                     
       print(f"Enter {N} real numbers:")                                          
       for i in range(N):                                                         
           while True:                                                            
               try:                                                               
                   x = float(input(f"Element {i + 1}: "))                         
                   T.append(x)                                                    
                   break                                                          
               except ValueError:                                                 
                   print("Invalid input. Please enter a valid real number.")      
                                                                                  
       print("Array:", T)                                                         
                                                                                  
       max_val = T[0]                                                             
       min_val = T[0]                                                             
       max_index = 0                                                              
       min_index = 0                                                              
                                                                                  
       for i in range(1, N):                                                      
           if T[i] > max_val:                                                     
               max_val = T[i]                                                     
               max_index = i                                                      
           if T[i] < min_val:                                                     
               min_val = T[i]                                                     
               min_index = i                                                      
                                                                                  
       print(f"Maximum: {max_val} at index {max_index}")                          
       print(f"Minimum: {min_val} at index {min_index}")                          
                                                                                  
   find_max_min_indices()                                                         
elif problem == 19 :      
    def evaluate_polynomial():                                                                  
        try:                                                                                    
            N = int(input("Enter the degree of the polynomial (non-negative integer): "))       
            if N < 0:                                                                           
                print("Error: Degree must be non-negative.")                                    
                return                                                                          
        except ValueError:                                                                      
            print("Invalid input. Please enter an integer.")                                    
            return                                                                              
                                                                                                
        coefficients = []                                                                       
        print(f"Enter {N + 1} coefficients from highest degree to lowest:")                     
        for i in range(N + 1):                                                                  
            while True:                                                                         
                try:                                                                            
                    coeff = float(input(f"Coefficient for x^{N - i}: "))                        
                    coefficients.append(coeff)                                                  
                    break                                                                       
                except ValueError:                                                              
                    print("Invalid input. Please enter a valid real number.")                   
                                                                                                
        try:                                                                                    
            x = float(input("Enter the value of x: "))                                          
        except ValueError:                                                                      
            print("Invalid input for x. Please enter a real number.")                           
            return                                                                              
                                                                                                
        result = coefficients[0]                                                                
        for i in range(1, N + 1):                                                               
            result = result * x + coefficients[i]                                               
                                                                                                
        print(f"P({x}) = {result:.6f}")                                                         
                                                                                                
    evaluate_polynomial()                                                                       
elif problem == 20 :      
    def matrix_operations():                                                             
        try:                                                                             
            L = int(input("Enter number of rows (positive integer): "))                  
            C = int(input("Enter number of columns (positive integer): "))               
            if L <= 0 or C <= 0:                                                         
                print("Error: Matrix dimensions must be positive.")                      
                return                                                                   
        except ValueError:                                                               
            print("Invalid input. Please enter integers for dimensions.")                
            return                                                                       
                                                                                         
        M = []                                                                           
        print(f"Enter {L} rows with {C} integers each:")                                 
        for i in range(L):                                                               
            row = []                                                                     
            while len(row) < C:                                                          
                try:                                                                     
                    x = int(input(f"Row {i + 1}, Column {len(row) + 1}: "))              
                    row.append(x)                                                        
                except ValueError:                                                       
                    print("Invalid input. Please enter an integer.")                     
            M.append(row)                                                                
                                                                                         
        print("\nMatrix:")                                                               
        for row in M:                                                                    
            print(row)                                                                   
                                                                                         
        total = sum(sum(row) for row in M)                                               
        print(f"\nTotal sum of all elements: {total}")                                   
                                                                                         
        print("Row sums:")                                                               
        for i, row in enumerate(M):                                                      
            print(f"Row {i + 1}: {sum(row)}")                                            
                                                                                         
        print("Column sums:")                                                            
        for j in range(C):                                                               
            col_sum = sum(M[i][j] for i in range(L))                                     
            print(f"Column {j + 1}: {col_sum}")                                          
                                                                                         
    matrix_operations()                                                                  
elif problem == 21 :      
    def matrix_operations():                                                              
        try:                                                                             
            N = int(input("Enter the order of the square matrix (positive integer): "))  
            if N <= 0:                                                                   
                print("Error: Matrix order must be positive.")                           
                return                                                                   
        except ValueError:                                                               
            print("Invalid input. Please enter an integer.")                             
            return                                                                       
                                                                                         
        # Read matrix A                                                                  
        A = []                                                                           
        print(f"Enter {N} rows with {N} integers each:")                                 
        for i in range(N):                                                               
            row = []                                                                     
            while len(row) < N:                                                          
                try:                                                                     
                    x = int(input(f"Row {i + 1}, Column {len(row) + 1}: "))              
                    row.append(x)                                                        
                except ValueError:                                                       
                    print("Invalid input. Please enter an integer.")                     
            A.append(row)                                                                
                                                                                         
        # Count non-zero elements                                                        
        nonzero_count = sum(1 for row in A for val in row if val != 0)                   
                                                                                         
        # Compute trace and diagonal product                                             
        trace = 0                                                                        
        diag_product = 1                                                                 
        for i in range(N):                                                               
            trace += A[i][i]                                                             
            diag_product *= A[i][i]                                                      
                                                                                         
        # Compute transpose                                                              
        A_T = [[A[j][i] for j in range(N)] for i in range(N)]                            
                                                                                         
        # Compute A^2                                                                    
        A2 = [[0 for _ in range(N)] for _ in range(N)]                                   
        for i in range(N):                                                               
            for j in range(N):                                                           
                for k in range(N):                                                       
                    A2[i][j] += A[i][k] * A[k][j]                                        
                                                                                         
        # Output results                                                                 
        print("\nOriginal Matrix A:")                                                    
        for row in A:                                                                    
            print(row)                                                                   
                                                                                         
        print(f"Number of non-zero elements: {nonzero_count}")                           
        print(f"Trace of A: {trace}")                                                    
        print(f"Product of diagonal elements: {diag_product}")                           
elif problem == 22 :      
    def matrix_to_vector():                                                     
        try:                                                                    
            L = int(input("Enter number of rows (positive integer): "))         
            C = int(input("Enter number of columns (positive integer): "))      
            if L <= 0 or C <= 0:                                                
                print("Error: Matrix dimensions must be positive.")             
                return                                                          
        except ValueError:                                                      
            print("Invalid input. Please enter integers for dimensions.")       
            return                                                              
                                                                                
        M = []                                                                  
        print(f"Enter {L} rows with {C} integers each:")                        
        for i in range(L):                                                      
            row = []                                                            
            while len(row) < C:                                                 
                try:                                                            
                    x = int(input(f"Row {i + 1}, Column {len(row) + 1}: "))     
                    row.append(x)                                               
                except ValueError:                                              
                    print("Invalid input. Please enter an integer.")            
            M.append(row)                                                       
                                                                                
        V = []                                                                  
        for row in M:                                                           
            V.extend(row)                                                       
                                                                                
        print("\nMatrix:")                                                      
        for row in M:                                                           
            print(row)                                                          
        print("\nVector (row-wise):")                                           
        print(V)                                                                
                                                                                
    matrix_to_vector()                                                          
elif problem == 23 :     
        print("note implemented yet")       
else:
    print("come on u can do better :/ ")
