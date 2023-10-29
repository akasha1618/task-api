import random
import textwrap
import pandas as pd

# lists for chat messages templates
names = ["Alice", "Bob", "Carol", "David", "Erin", "Frank", "Georgia", "Harry"]
software_issues = [
    "can't install Adobe Illustrator due to license errors",
    "Microsoft Teams not syncing messages",
    "AutoCAD crashing on large file loads",
    "Outlook not sending emails with attachments",
    "Zoom meetings dropping frequently",
    "Slack notifications not working",
    "Browser keeps redirecting to unwanted ads",
    "Salesforce login giving authentication error"
]
hardware_issues = [
    "external hard drive not recognized",
    "printer showing 'out of ink' despite new cartridges",
    "laptop screen flickering intermittently",
    "keyboard missing keystrokes",
    "mouse scroll wheel unresponsive",
    "webcam showing very dark images",
    "smartphone overheating during calls",
    "desk phone not dialing out"
]
general_it_issues = [
    "VPN disconnects every hour",
    "Wi-Fi signal very weak in conference room",
    "guest network password not working",
    "unable to reset user password in admin portal",
    "email groups not updating members",
    "data sync between CRM and ERP systems failing",
    "access control reader at main door malfunctioning",
    "projector not displaying presentations"
]
questions = [
    "Any suggestions on what to do next?",
    "Can someone from IT look into this?",
    "What could be causing this?",
    "Is this a known issue?",
    "How can I fix this myself?",
    "Do I need to submit a formal ticket for this?",
    "Who is the best person to contact for help?",
    "Could this be fixed remotely, or do I need a technician?"
]
details = [
    "This issue started this morning.",
    "It's impacting my work significantly.",
    "I've already tried the basic troubleshooting steps.",
    "This only happens with my account.",
    "I noticed this after the recent system update.",
    "This is critical for my tasks today.",
    "Other colleagues are facing the same problem.",
    "I haven't changed any settings recently."
]

# Generate the chat messages
def generate_chat_message():
    name = random.choice(names)
    issue_type = random.choice(["software difficulty", "hardware issue", "general IT problem"])
    if issue_type == "software issue":
        issue = random.choice(software_issues)
    elif issue_type == "hardware issue":
        issue = random.choice(hardware_issues)
    else:
        issue = random.choice(general_it_issues)
    
    question = random.choice(questions)
    detail = random.choice(details)

    # multiple templates
    templates = [
        f"Hi, this is {name}. I've run into a {issue_type} : {issue}. {detail} Can anyone assist?",
        f"Need help! {name} here and I have a {issue_type} I don't know what to do - specifically, {issue}. {question}",
        f"Quick issue from {name}: There's a {issue_type} problem where {issue}. {detail} {question}",
        f"Can someone check this? My name is {name} I am reporting a {issue_type}. To be specific, {issue}. {question}",
        f"{name} in trouble with a {issue_type}. It's about {issue}. {detail} What's the best way forward?",
        f"{name} on the line with a {issue_type}: {issue}. Happened just now. {question}",
        f"My name is {name}'s I have a big {issue_type}. The problem is {issue}. {detail} Suggestions?",
        f"Hey, it's {name} and I really don't know how to hande a {issue_type} again. This time it's {issue}. {question} Anyone free to help?"
    ]

    return random.choice(templates)

# Generating 444 example chat messages
example_chat_messages = [generate_chat_message() for _ in range(444)]



greetings = [
        "Dear IT Team,",
        "Hello there,",
        "Good day,",
        "Hi Tech Support,"
        "Greetings IT Support,"
        "Hi IT Helpdesk,"
        "To the IT Department,"
        "Attention, Tech Team,"
    ]
sign_offs = [
        "Thanks and regards,",
        "Appreciatively,",
        "Sincerely,",
        "Best,"
        "Good day,"
        "Thanks,"
        "Good night,"
        "Regards,"
    ]
    # Variations for the introductory and concluding sentences
introductions = [
    "I'm writing with a concern regarding",
    "I've encountered a problem with",
    "There seems to be an issue with",
    "I need assistance with",
    "I'm facing a challenge with"
    ]
conclusions = [
    "Would you mind providing some assistance?",
    "I'd really appreciate some guidance on this.",
    "Could you advise on how to proceed?",
    "I'm looking forward to your advice on this matter.",
    "Your support on this would be very helpful."
    ]   

senders = ["Alice", "Bob", "Carol", "David", "Fiona", "Hannah", "Greg", "Ethan" ]
    
issues = [
    {
        "subject": "difficulty accessing the shared network drive",
        "detail": "Each attempt results in a timeout error, despite the network being otherwise fine."
    },
    {
        "subject": "video conferencing tool not functioning",
        "detail": "My microphone and camera are on, but others can't hear or see me during meetings."
    },
    {
        "subject": "lost document recovery",
        "detail": "I was working on a report when my system crashed, and now I can't find the file."
    },
    {
        "subject": "slow computer performance",
        "detail": "My system has become extremely sluggish, particularly when opening large files or using certain software."
    },
    {
        "subject": "frequent software freezing",
        "detail": "Programs like Word and Excel keep freezing randomly, forcing me to restart them often."
    },
    {
        "subject": "error messages when opening emails",
        "detail": "Every time I try to open certain emails, I get an error saying 'The item cannot be displayed'."
    },
    {
        "subject": "unresponsive touchscreen on the smartboard",
        "detail": "The touchscreen doesn't respond to touch or pen inputs during presentations."
    },
    {
        "subject": "VPN setup issues on laptop",
        "detail": "I'm unable to configure the VPN settings as per the instructions provided."
    },
    {
        "subject": "security alert notifications",
        "detail": "I keep receiving pop-up messages about potential security threats, though I haven't downloaded anything suspicious."
    },
    {
        "subject": "sync problems with cloud storage",
        "detail": "Files I place in my cloud folder aren't syncing across my devices as they should."
    }
    ]


# Generate a number of chat messages and email bodies
def generate_unique_email_body():
    greeting = random.choice(greetings)
    sign_off = random.choice(sign_offs)
    introduction = random.choice(introductions)
    conclusion = random.choice(conclusions)
    sender = random.choice(senders)
    issue = random.choice(issues)
    sender = random.choice(["Alice", "Bob", "Carol", "David"])
    email_body = f"{greeting}{introduction} {issue['subject']}. {issue['detail']}\n\n{conclusion}\n\n{sign_off}\n{sender}"
    return(email_body)

# Generating 444 example chat messages
example_email_bodies = [generate_unique_email_body() for _ in range(444)]
# Combine chat messages and email bodies into one dataset
combined_dataset = example_chat_messages + example_email_bodies

# Shuffle the combined dataset to mix chat messages and email bodies
random.shuffle(combined_dataset)

 # Creating a DataFrame
df = pd.DataFrame(combined_dataset, columns=["Description"])

# Saving the DataFrame to a CSV file
csv_file_path = "it_support_all.csv"
df.to_csv(csv_file_path, index=False)
