
### 📄 `README.md`

# Support Ticket Analyzer

Hi! I'm **Sabrin Khatib**, and this is my solution for the **Junior Full Stack Home Assignment** — specifically, **Option 1: Support Ticket Analyzer**.

This command-line Python tool analyzes support tickets from a JSON file by:
- Categorizing them based on common keywords
- Summarizing how many tickets fall into each category
- Showing tickets created before a user-specified date

---

## Features

- Parses support tickets from `tickets.json`
- Categorizes tickets using keyword matching
- Displays a summary of categories (e.g., login, bug, payment)
- Filters and shows tickets created before a given date

---

## 🛠️ Technologies Used

- **Language**: Python 3
- **Libraries**: Only standard Python libraries (`json`, `datetime`, `collections`, `string`)

---

## 📁 File Structure

support-ticket-analyzer/
├── support_ticket_analyzer.py        # Main Python script
├── tickets.json          # Input file with ticket data
└── README.md             # Project documentation


## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Place all files in the same directory.
3. Open a terminal in that directory and run:
   support_ticket_analyzer.py        


5. When prompted, enter a date in the format:

YYYY-MM-DD

The program will then:
- Print a summary of ticket categories
- List all tickets created before the specified date

---

## Example Ticket Format (tickets.json)

```
{
  "tickets": [
    {
      "ticketId": "T1001",
      "subject": "Login issue",
      "description": "User cannot login due to forgotten password.",
      "status": "open",
      "created_at": "2025-03-25T10:30:00Z"
    }
  ]
}
```


## 👩‍💻 About Me

I'm **Sabrin Khatib**, a junior developer with a strong interest in practical problem-solving, clean code, and backend-focused development.
[LinkedIn Profile](https://www.linkedin.com/in/sabrin-khatib-802a96252/)

Thank you for reviewing my submission!
