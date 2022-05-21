from instapy import InstaPy

usr = input("enter username")
pwd = input("enter password")
session = InstaPy(geckodriver_path='/Users/berkealtiparmak/Desktop/InstagramBot/geckodriver',
                  username=usr, password=pwd,
                  headless_browser=True,
                  want_check_browser=False)
session.login()
session.like_by_tags(["bmw", "mercedes"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["nice!", "cool"])
