# brute-force-cryptowallet
- This is a tool for those of you who've somehow lost your Ethereum wallet password. 
- It's essentially a stripped-down version of [pyethsaletool](https://github.com/ethereum/pyethsaletool).  In addition you can have passwords be read from a newline-delimited file, and/or provide a specification to be used to generate passwords. The multiprocessing library `joblib` is used to test out passwords using all the cores on your machine. 
- This tool is compatible with both Python 2 and Python 3. It depends on the following libraries
    
    joblib
    bitcoin

## Summary

    Usage: pyethrecover.py [options]
    
    Options:
      -h, --help            show this help message and exit
      -p PW, --password=PW  A single password to try against the wallet.
      -f PWFILE, --passwords-file=PWFILE
                            A file containing a newline-delimited list of
                            passwords to try. (default: none)
      -s PWSFILE, --password-spec-file=PWSFILE
                            A file containing a password specification
      -w WALLET, --wallet=WALLET
                            The wallet against which to try the passwords.
                            (default: wallet.json)
    

Example1
=======

Let's say you have a wallet file named `ethereum-wallet.json` protected by the password `correct horse battery staple`. You enter your guesses into a file named `passwords.txt`, like so:

    shelly sells seashells down by the seashore
    It was the best time of times, it was the worst of times...
    Password1
    correct horse battery staple
    mean mr mustard sleeps in the park

If you run the utility like so...

    ./pyethrecover.py -w ethereum-wallet.json -f passwords.txt

...you should get back something like this:

    shelly sells seashells down by the seashore
    It was the best time of times, it was the worst of times...
    Password1
    correct horse battery staple

    Your seed is:
    abc123abc123...

    Your password is:
    correct horse battery staple

Example2
=======
Let's say you have a wallet file named `ethereum-wallet.json` 
and you remember that you password is a greeting in some 
language followed by the name of an american president. 
Say you're not sure if the president is addressed with a title, 
but if he is you're certain it's either "president" or "mister". 
You would create a file `password_spec.txt` like so ...

    [
        ('hello', 'bonjour', 'hola'),
        ('', 'mister', 'president'),
        ('smith', 'jefferson')
    ]

and call it like so...

    ./pyethrecover.py -w ethereum-wallet.json -s password_spec.txt

Check out the comments in the `password_spec.txt` file for more details
