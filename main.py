import sys, scraper, webbrowser
from scraper import Facebook

def main():
    # Check the arguments
    if len(sys.argv) != 4:
        usage()
    user = sys.argv[1]
    passw = sys.argv[2]
    email = sys.argv[3]

    print "Initializing.."
    f = Facebook(user, passw)
    # Log the user
    f.login()
    # Fetch profile details
    profile_link = f.profile(email)
    print "Facebook Profile URL:", profile_link
    webbrowser.open(profile_link);

def usage():
    '''
        Usage: main.py user@domain.tld password email_id
        'email_id' for which the user profile needs to be queried
    '''
    print 'Usage: ' + sys.argv[0] + ' user@domain.tld password email_id'
    sys.exit(1)

if __name__ == '__main__':
    main()