import requests
import re
import random

quotes = [
    "Code is like humor. When you have to explain it, it's bad. – Cory House",
    "First, solve the problem. Then, write the code. – John Johnson",
    "Experience is the name everyone gives to their mistakes. – Oscar Wilde",
    "In order to be irreplaceable, one must always be different. – Coco Chanel",
    "Java is to JavaScript what car is to Carpet. – Chris Heilmann",
    "Knowledge is power. – Francis Bacon",
    "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday's code. – Dan Salomon",
    "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away. – Antoine de Saint-Exupéry",
    "Ruby is rubbish! PHP is phpantastic! – Nikita Popov",
    "Code never lies, comments sometimes do. – Ron Jeffries",
    "Fix the cause, not the symptom. – Steve Maguire",
    "Optimism is an occupational hazard of programming. – Kent Beck",
    "When to use iterative development? You should use iterative development only on projects that you want to succeed. – Martin Fowler",
    "Simplicity is the soul of efficiency. – Austin Freeman",
    "Before software can be reusable it first has to be usable. – Ralph Johnson",
    "Make it work, make it right, make it fast. – Kent Beck",
    "The best error message is the one that never shows up. – Thomas Fuchs",
    "There are only two hard things in Computer Science: cache invalidation and naming things. – Phil Karlton",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. – Martin Fowler",
    "It's not a bug — it's an undocumented feature. – Anonymous",
    "Talk is cheap. Show me the code. – Linus Torvalds",
    "Programs must be written for people to read, and only incidentally for machines to execute. – Harold Abelson",
    "The most disastrous thing that you can ever learn is your first programming language. – Alan Kay",
    "The function of good software is to make the complex appear to be simple. – Grady Booch",
    "Truth can only be found in one place: the code. – Robert C. Martin",
    "One of the best programming skills you can have is knowing when to walk away for a while. – Oscar Godson",
    "The art of programming is the art of organizing complexity. – Edsger W. Dijkstra",
    "Debugging is twice as hard as writing the code in the first place. – Brian W. Kernighan",
    "Weeks of coding can save you hours of planning. – Anonymous",
    "The best way to predict the future is to invent it. – Alan Kay"
]

quote = random.choice(quotes)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_quote = f"> 💡 {quote}"

updated = re.sub(
    r'<!--QUOTE_START-->.*?<!--QUOTE_END-->',
    f'<!--QUOTE_START-->\n{new_quote}\n<!--QUOTE_END-->',
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)

print(f"Quote updated: {quote}")
