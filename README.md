# Get AWS CLI Profiles
I have a terrible memory. I also manage a lot of AWS accounts. I get tired of knowing the name of the accounts as I utilize the AWS CLI. The solution...about 20 line of Python! The script looks through your AWS config file and returns the a list of accounts.

Here are a few things you should know if you want to use this:
* This has only been tested on a Mac.
* Assumes your AWS config file is in the .aws folder, and that your .aws folder is in your home folder (~).
* That you adhere to best practices and don't put your keys and/or secrets in your config file, that is what the credentials file is for. Seriously don't do it!

**BONUS**: I make 'getawscliprofiles.py' executable (chmod +x) and create a symbolic link in '/usr/local/bin/' and name it 'awsprofiles'.

For example:
`ln -s /path/to/getawscliprofiles/getawscliprofiles.py /usr/local/bin/awsprofiles`

Now I just type 'awsprofiles' anywhere in my terminal, and bam...there are all my AWS profiles!

Using the example config file, the out put would look like this:
```
default
Netflix - Production
Google - Production
Recipe for Dr. Pepper - Production
```
