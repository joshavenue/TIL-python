def add(x, y):            // Define a function with 2 argument //
    try:                  // Try to run codeblock if it can be converted from Int to Float
        a = float(x)
        b = float(y)
        total = a + b     // Add them together //
    except ValueError:    // If it is not a number, it will tells the system to return nothing //
        return None
    else:
        return total      // If the try statement works and input is an integer, it will return the total //
