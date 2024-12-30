Explanation:
	1.	Negative Lookahead ((?!...)):
	•	The pattern (?!exclude\.com\b) ensures that the domain exclude.com is not matched.
	2.	Full Regex:
	•	\b[A-Za-z0-9._%+-]+@: Matches the username part of the email.
	•	(?!exclude\.com\b): Ensures the domain is not exclude.com.
	•	[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b: Matches the domain part of the email.

Output:

For the given input text:

['user1@domain.com', 'user3@domain.com']

This ensures that emails from exclude.com are excluded while all other valid email addresses are extracted.
