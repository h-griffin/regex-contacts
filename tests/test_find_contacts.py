
from find_contacts import __version__
import pytest
import pyperclip, re
from find_contacts.find_contacts import find_contacts


def test_version():
    assert __version__ == '0.1.0'

def test_1():
    pyperclip.copy('123-456-7890 test@test.com')
    text = str(pyperclip.paste())

    actual = find_contacts(text)
    expected = '123-456-7890 test@test.com'
    assert actual == expected

# def test_2():
#     pyperclip.copy('''Icon of a person: white decorative
#     Got It
#     This website uses cookies to improve your experience. Learn More
#     Skip to main content
#     Home
#     Search form
#     Search
#     Catalog
#     Blog
#     Media
#     Write for Us
#     About Us
#     Contact Us
#     We are currently shipping with some delays. Please see our FAQ.

#     Topics
#     Art & Design
#     General Computing
#     Hacking & Computer Security
#     Hardware / DIY
#     Kids
#     LEGO®
#     Linux & BSD
#     Manga
#     Programming
#     Python
#     Science & Math
#     Scratch
#     System Administration
#     Early Access
#     Free ebook edition with every print book purchased from nostarch.com!
#     Shopping cart
#     0 Items	Total: $0.00
#     User login
#     Log in
#     Create account
#     Contact Us

#     No Starch Press, Inc.
#     245 8th Street
#     San Francisco, CA 94103 USA
#     Phone: 800.420.7240 or +1 415.863.9900 (9 a.m. to 5 p.m., M-F, PST)
#     Fax: +1 415.863.9950

#     Reach Us by Email

#     General inquiries: info@nostarch.com
#     Media requests: media@nostarch.com
#     Academic requests: academic@nostarch.com (Further information)
#     Help with your order: info@nostarch.com
#     Reach Us on Social Media
#     Twitter
#     Facebook
#     Instagram
#     Linkedin
#     Pinterest

#     Navigation
#     My account
#     Want sweet deals?
#     Sign up for our newsletter.


#     About Us  |  Jobs!  |  Sales and Distribution  |  Rights  |  Media  |  Academic Requests  |  Conferences  |  FAQ  |  Contact Us  |  Write for Us  |  Privacy
#     Copyright 2020. No Starch Press, Inc''')

#     actual = find_contacts()
#     expected = '''
#         800-420-7240
#         415-863-9900
#         415-863-9950
#         info@nostarch.com
#         media@nostarch.com
#         academic@nostarch.com
#         info@nostarch.com'''
#     assert actual == expected


