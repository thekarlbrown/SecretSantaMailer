# SecretSantaMailer
Tool that takes a formatted text file for Secret Santa use, generates Secret Santa's, then emails individuals their secret Santa.

The format that the emails need to be added in is listed in the supplied emailList.txt. Please edit as necessary. Any additional email's after the first are email's that cannot match with the first email.

Example:

karlbrownthinks@gmail.com

test@gmail.com

*

means that karlbrownthinks@gmail.com cannot match with test@gmail.com

There also must be a SMTP and TLS enabled email server and account provided. This is passed in via the command line. 

An email account (karlbrownthinks@gmail.com), password (FAKEpass123), server (smtp.gmail.com), and port (587) must be provided.

If you are using Gmail, you will need to enable access for less secure apps: https://www.google.com/settings/security/lesssecureapps
