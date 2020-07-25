#all the functions needed for the coffee bot.
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
      return 'small'
  elif res == 'b':
      return 'medium'
  elif res == 'c':
      return 'large'
  else:
      print_message()
      return get_size()
def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  if res == 'a':
      return 'latte'
  elif res == 'b':
      return 'non-fat latte'
  elif res == 'c':
      return 'soy latte'
  else:
      print_message()
      return order_latte()

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')

  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return order_mocha()
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_mocha():
 while True:
  res = input("Would you like to try out limited-edition peppermint mocha? \n[a] sure! \n[b] Mabye next time!")
  if (res == "a"):
    return "Peppermint Mocha"
  elif (res == "b"):
    return "Mocha"
  print_message()



#the actual coffee bot
def coffee_bot():
    print('Welcome to the cafe!')

    size = get_size()
    drink_type = get_drink_type()

    drink = '{} {}'.format(size, drink_type)
    print('Alright, that\'s a {}!'.format(drink))

    name = input('Can I get your name please? \n> ')
    print('Thanks, {}! Your order will be ready shortly.'.format(name))

    order_drink = input("Would you like to order another drink? y/n")
    if (order_drink == "n"):
        print("Thank you for your buisness!")
    if (order_drink == "y"):
        coffee_bot()
    else:
        print("Please enter the letter ""y"" or the letter ""n"" without any capitals or spaces.")


#call the bot
coffee_bot()