import json
from datetime import datetime
from collections import defaultdict
import string


"""
categorizing tickets by common keywords
"""
categories = {
    "login" :["login" , "log in", "sign in", "authentication"],
    "payment":["payment" , "pay" ,"credit card", "checkout","transaction", "billing"],
    "bug": ["bug", "error", "issue", "fail", "crash","glitch"],
    "feature request": ["feature", "request", "add", "option"],
    "performance": ["slow", "response time", "lag", "performance"],
    "account issues": ["password", "account", "profile", "credentials"],
    "other": []

}

"""
This function is responsible for loading support ticket data from a JSON file.
Returns the list of tickets found under the "tickets" key.
"""
def load_tickets(jsonfile):
    try:
        with open(jsonfile, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("tickets", [])
    except Exception as e:
        print(f"Error loading file: {e}")
        return []

"""
this function converts text to lowercase, remove punctuation, and split into words.
"""
def clean_text_to_words(text):
    if not text:
        return []

    cleaned = ""
    for char in text:
        if char not in string.punctuation:
            cleaned += char.lower()

    return cleaned.split()

"""
The function is used to convert a date string into a Python datetime object, trying multiple formats.
It returns a datetime object.
"""
def parse_date_from_string(date_str):
    formats = [
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%d",
        "%Y/%m/%d %H:%M:%S",
        "%B %d, %Y %H:%M"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None #in case no format matched

"""
Categorizes a ticket based on keywords in subject and description.
Returns the first matching category or "other" if no match is found.
"""
def categorize_ticket(subject , description):
   words = clean_text_to_words(subject+ " "+ description)
   for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in words:
                return category
   return "other"

"""
Categorizes all tickets and counts categories.
Returns a list of categorized tickets and a summary dictionary.
"""
def categorize_all_tickets(tickets):
    summary = defaultdict(int)
    categorized = []

    for ticket in tickets:
        subject = ticket.get("subject", "")
        description = ticket.get("description", "")
        category = categorize_ticket(subject, description)
        ticket["category"] = category
        summary[category] += 1
        categorized.append(ticket)

    return categorized, summary

def load_and_parse_tickets(filename):
    tickets = load_tickets(filename)
    if not tickets:
        print("No tickets found")
        exit()
    return tickets

def print_category_summary(summary):
    print("Summary of the tickets:")
    for category, count in summary.items():
        name = category.capitalize()
        if count == 1:
            print(f"There is 1 ticket about {name}.")
        else:
            print(f"There are {count} tickets about {name}.")


def prompt_user_date():
    date_input = input("Enter a date (in YYYY-MM-DD format) to see tickets created before that date: ")
    try:
        return datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date, please follow this format : YYYY-MM-DD.")
        exit()

def show_tickets_before_date(tickets, user_date):
    print(f" *** Tickets Before {user_date.date()} ***")
    for ticket in tickets:
        created = parse_date_from_string(ticket.get("created_at", ""))
        if created and created < user_date:
            subject = ticket.get("subject", "(No Subject)")
            print(f"- [{ticket['ticketId']}] {subject} | Created at: {ticket['created_at']} | Category: {ticket['category']}")

def main():
    tickets = load_and_parse_tickets("tickets.json")
    categorized_tickets, summary = categorize_all_tickets(tickets)
    print_category_summary(summary)
    user_date = prompt_user_date()
    show_tickets_before_date(categorized_tickets, user_date)
