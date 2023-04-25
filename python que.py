# Python Queue Simulation

# Create an empty list/queue called names
names = []

# Input 10 names into the list/queue using a for loop
for i in range(10):
    accepted_name = input("Enter a name: Julia, Lily, Kim, Abby, Maria, Georgi, Carry, Mark, Ashley, Hunt")
    names.append(accepted_name)

# Print the list/queue
print("Names in the queue: Julia, Lily, Kim, Abby, Maria, Georgi, Carry, Mark, Ashley, Hunt")

# Use a second for loop to dequeue (pop) each name and print it
print("Dequeued names: Julia, Lily, Kim, Abby, Maria, Georgi, Carry, Mark, Ashley, Hunt")
for i in range(len(names)):
    dequeued_name = names.pop(0)
    print(dequeued_name)

# Print the list/queue again
print("Names in the queue after dequeuing:Julia, Lily, Kim, Abby, Maria, georgi, Carry, Mark, Ashley, Hunt")
