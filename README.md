<h1>CS361-Microservice </h1>
<h2>Communication Contract</h2>
<h3>How to request data</h3>
To recieve data from the email microservice there will be a file actively running that will await a text file sendmail.txt to contain the word 'yes\n'. 
Once the file has the word yes inside it the email client will generate an email looking for a file to attach named generatedQR.png.
<h3>How to recieve data</h3> 
The way to view data from the email micro service will be to check the command line for 'Email Sent' to comfirm data has been transfered. Then to verify check
the email that was designated in the application to recieve the generated QR code. 
