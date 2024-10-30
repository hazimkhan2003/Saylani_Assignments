# Scenario 1: Grocery Shopping List
# You are creating a program to manage a grocery shopping list. Users should be able to add items, 
# remove items, and display the current list.
# Scenario 3: Word Frequency Counter
# You are given a list of words, and you need to count the frequency of each word.
# word_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]

# Grocery Shopping List
shopping_list = []

# Add item to the list
def add_item(item):
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

# Remove item from the list
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} is not in the list.")

# Display the current shopping list
def display_list():
    if shopping_list:
        print("Current shopping list:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")

add_item("Milk")
add_item("Bread")
remove_item("Milk")
display_list()

# Scenario 2: Student Grades
# You are managing student grades using a dictionary. You need to calculate the average grade.take 
# atleast 5 Students grades & then calculate the average.

# Student Grades
grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Eve": 88
}

# Calculate average grade
def calculate_average(grades):
    total = sum(grades.values())
    average = total / len(grades)
    return average

# Display average grade
average_grade = calculate_average(grades)
print(f"Average grade: {average_grade:.2f}")

# Scenario 3: Password Strength Checker
# You are creating a program to check the strength of passwords based on certain criteria.
# • Password should be at least 8 characters long.
# • Password should contain at least one digit.
# • Password should contain at least one letter.
# Word Frequency Counter
word_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]

# Count word frequency
def count_frequency(words):
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Display word frequencies
word_frequencies = count_frequency(word_list)
for word, count in word_frequencies.items():
    print(f"{word}: {count}")

# Scenario 04: Voting System (Annual Employee Recognition Awards)
# You are developing a simple voting system for a contest. Users can vote for their Favorite option, and 
# you need to count the votes.
# In a corporate setting, the HR department is organizing the Annual Employee Recognition Awards, 
# where employees get the opportunity to vote for their colleagues nominated in different categories. 
# The HR team has decided to use a simple voting system to collect and tally votes for the nominees in 
# various award categories. The script provided will be utilized for this purpose.
# Candidates: The nominees for different award categories, such as "Employee of the Year," "Team 
# Player of the Year," and "Innovation Award," are represented by the list of candidates: 'Candidate A,' 
# 'Candidate B,' and 'Candidate C.'
# Voting Process: Employees are requested to input the number of voters participating in the awards. 
# Each voter is presented with a list of nominees, and they can vote for their preferred candidate by 
# entering the corresponding number.
# Validation: The script ensures that the entered vote is within the valid range of candidates. If an 
# employee enters an invalid vote, the system prompts them to choose a valid candidate.
# Recording Votes: The script records each vote for the selected candidate and prints a confirmation 
# message indicating that the vote has been recorded.
# Results Display: Once all votes are collected, the system displays the voting results, showing the 
# number of votes each candidate received in each category.
# Award Winners: Based on the voting results, the HR department can identify the winners for each 
# award category and proceed with recognizing and rewarding the selected employees during the 
# Annual Employee Recognition Ceremony.
# This script provides a straightforward and transparent way for employees to participate in the 
# recognition process, fostering a sense of engagement and community within the organization. The 
# HR team can use the collected votes to acknowledge and appreciate the efforts of outstanding 
# employees in various aspects of their work.

# List of candidates
candidates = ["Candidate A", "Candidate B", "Candidate C"]
# Dictionary to store votes for each candidate
votes = {candidate: 0 for candidate in candidates}
# Function to display candidates and take votes
def voting_process(num_voters):
    print("Candidates:")
    for idx, candidate in enumerate(candidates, start=1):
        print(f"{idx}. {candidate}")
        # Record votes
    for voter in range(1, num_voters + 1):
        while True:
            try:
                vote = int(input(f"\nVoter {voter}, please enter the number of your preferred candidate (1-{len(candidates)}): "))
                if 1 <= vote <= len(candidates):
                    selected_candidate = candidates[vote - 1]
                    votes[selected_candidate] += 1
                    print(f"Vote recorded for {selected_candidate}.")
                    break
                else:
                    print(f"Invalid input. Please enter a number between 1 and {len(candidates)}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Function to display the voting results
def display_results():
    print("\nVoting Results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")
    # Determine the winner
    max_votes = max(votes.values())
    winners = [candidate for candidate, count in votes.items() if count == max_votes]
    # Display the winner(s)
    if len(winners) > 1:
        print("\nIt's a tie between: " + ", ".join(winners))
    else:
        print(f"\nThe winner is: {winners[0]}")

# Main logic
def main():
    try:
        num_voters = int(input("Enter the number of voters: "))
        if num_voters <= 0:
            print("The number of voters must be greater than zero.")
            return
        
        voting_process(num_voters)
        display_results()

    except ValueError:
        print("Invalid input. Please enter a valid number of voters.")

# Run the program
if __name__ == "__main__":
    main()
