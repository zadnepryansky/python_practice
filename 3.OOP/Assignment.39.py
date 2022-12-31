class BigPost:

    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


post_about_life = BigPost('Alice', 'Hello world!', 500)
post_about_war = BigPost('Andrew', 'War is bed!', 999)

post_about_life.number_of_likes = 600
post_about_war.number_of_likes = 1999

print(post_about_war.number_of_likes)
print(post_about_life.number_of_likes)
print(post_about_life.text)
print(post_about_war.text)
