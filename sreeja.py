import os
import streamlit as st

# Sample workout plans
sample_workout_plans = """
Monday:
- Squats: 3 sets of 10 reps
- Bench Press: 3 sets of 10 reps
- Pull-ups: 3 sets of 8 reps

Wednesday:
- Deadlifts: 3 sets of 8 reps
- Military Press: 3 sets of 10 reps
- Bent-over Rows: 3 sets of 10 reps

Friday:
- Lunges: 3 sets of 12 reps (each leg)
- Dumbbell Flyes: 3 sets of 10 reps
- Lat Pulldowns: 3 sets of 10 reps
"""

# Function to get user's personal details including membership details and set workout goals
def get_personal_details_and_goals():
    st.subheader("Set Workout Goals:")
    goals = st.radio("", ["Build Muscle", "Lose Weight", "Increase Endurance"])
    if st.button("Save Goals"):
        with open("workout_goals.txt", "a") as f:
            f.write(f"{goals}\n")
        st.success("Workout goals saved successfully.")

    st.subheader("Enter Personal Details:")
    name = st.text_input("Enter your name:")
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
    age = st.number_input("Enter your age:")
    membership_status = st.radio("Select membership status:", ["Active", "Inactive"])
    membership_type = st.selectbox("Select membership type:", ["Basic", "Standard", "Premium"])
    
    if st.button("Save Personal Details"):
        if name and age:
            with open("personal_details.txt", "a") as f:
                f.write(f"Name: {name}\nGender: {gender}\nAge: {age}\n")
                f.write(f"Membership Status: {membership_status}\nMembership Type: {membership_type}\n\n")
            st.success("Personal details saved successfully.")
        else:
            st.error("Please fill in all fields.")

# Function to display workout plans
def display_workout_plans():
    st.subheader("Workout Plans:")
    st.text(sample_workout_plans)

# Function to process payments
def process_payments():
    st.subheader("Select your package:")
    packages = ["Basic", "Standard", "Premium"]
    package = st.selectbox("", packages)
    if st.button("Process Payment"):
        prices = {"Basic": 50, "Standard": 100, "Premium": 150}
        amount = prices.get(package)
        if amount:
            st.write(f"Amount to be paid: ${amount}")
            st.success(f"Processing payment of ${amount} for {package} package.")
            if st.button("Confirm Payment"):
                st.success("Payment successful!")
                with open("membership.txt", "a") as f:
                    f.write(f"Membership Status: Active\nMembership Type: {package}\n")
        else:
            st.error("Invalid package selection.")

# Function to view membership details
def view_membership_details():
    if os.path.exists("personal_details.txt") and os.path.exists("membership.txt"):
        with open("personal_details.txt", "r") as f:
            personal_details = f.read()
        with open("membership.txt", "r") as f:
            membership_details = f.read()
        st.subheader("Membership Details:")
        st.text(personal_details)
        st.text(membership_details)
    else:
        st.write("No membership details found.")

# Function to update progress
def update_progress():
    name = st.text_input("Enter your name:")
    progress = st.text_area("Enter your progress:")
    if st.button("Save Progress"):
        if name and progress:
            with open(f"{name}_progress.txt", "a") as f:
                f.write(f"{progress}\n")
            st.success("Progress saved successfully.")
        else:
            st.error("Please fill in all fields.")

# Function to track progress
def track_progress():
    name = st.text_input("Enter your name:")
    if os.path.exists(f"{name}_progress.txt"):
        with open(f"{name}_progress.txt", "r") as f:
            progress = f.read()
        st.subheader(f"{name}'s Progress:")
        st.text(progress)
    else:
        st.write(f"No progress tracked for {name} yet.")

# Function to leave feedback
def leave_feedback():
    name = st.text_input("Enter your name:")
    feedback = st.text_area("Leave your feedback here:")
    if st.button("Submit Feedback"):
        if name and feedback:
            with open(f"{name}_feedback.txt", "a") as f:
                f.write(f"{feedback}\n")
            st.success("Thank you for your feedback!")
        else:
            st.error("Please fill in all fields.")

# Main function
def main():
    # Create files if they do not exist
    files = ["personal_details.txt", "workout_goals.txt", "membership.txt"]
    for file in files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                pass

    st.title("Custom Workout Planning System")
    choice = st.sidebar.selectbox("Select an option:", ["Set Workout Goals and Provide Personal Details",
                                                        "Display Workout Plans",
                                                        "Process Payments",
                                                        "View Membership Details",
                                                        "Update Progress",
                                                        "Track Progress",
                                                        "Leave Feedback"])

    if choice == "Set Workout Goals and Provide Personal Details":
        get_personal_details_and_goals()
    elif choice == "Display Workout Plans":
        display_workout_plans()
    elif choice == "Process Payments":
        process_payments()
    elif choice == "View Membership Details":
        view_membership_details()
    elif choice == "Update Progress":
        update_progress()
    elif choice == "Track Progress":
        track_progress()
    elif choice == "Leave Feedback":
        leave_feedback()

if __name__ == "__main__":
    main()
