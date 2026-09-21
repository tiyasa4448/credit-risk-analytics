print("Welcome to the Text Printer Simulator!")

# Create an empty list to store lines of text
print_queue = []

while True:
    line = input('Enter a line of text to add to the print queue (enter "quit" to print and exit):\n> ')

    if line.lower() == 'quit':
        if print_queue:
            print("\nPrinting...\n")
            for i, printed_line in enumerate(print_queue, start=1):
                print(f"Printing {i}: {printed_line}")
        else:
            print("No lines to print.")
        break
    else:
        # Add the line to the print queue
        print_queue.append(line)

