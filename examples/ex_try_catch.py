import sys
import traceback


# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    i
    # raise IndexError("This is an index error")
except IndexError as e:
    # Pass is just a no-op. Usually you would do recovery here.
    pass
except (TypeError, NameError):
    # Multiple exceptions can be handled together, if required.
    traceback.print_exc()

    pass
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:  # Execute under all circumstances
    print("We can clean up resources here")
