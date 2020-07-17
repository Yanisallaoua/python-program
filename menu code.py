import time


def menu_display():
	global menu
	menu = {1: '1- Double cheese burger',
		 2: '2- Poutine',
		 3: '3- Pizza',
		 4: '4- Fish tacos',
		 5: '5- Buffalo wings',
		 6: '6- Onion rings',
		 7: '7- Tomato soup',
		 8: '8- Turkey sandwich'}
	print('----------MC QUEEN MENU----------')
	for meal in menu.values():
		print(meal)
	print('------------------------------')
	print('C to complete the order')
	print('Q to quit or cancel the order')
	print('------------------------------')

def ordered_meals():
	for meal in order:
		print(meal[1:])


order_number = 1
meals_numbers = ['1','2','3','4','5','6','7','8']
order = []
running = True

while running:

	menu_display()
	print('Choose a meal to order from the list and press the correct number:')
	user_input = input()
	if user_input == 'q' or user_input == 'Q':
		print('The order is successfully cancelled')
		running = False
		break

	elif user_input == 'c' or user_input == 'C':
		print('Order complete, here is a list of your meals:')
		ordered_meals()
		print(f'Order number: ({order_number}) received, thank you!')
		order_number += 1
		order.clear()
		print('Press "N" to begin a new order:')
		user_input1 = input()
		if user_input1 == 'n' or user_input1 == 'N':
			continue

	elif user_input not in meals_numbers:
		print('********** The number entered is not correct **********')
		time.sleep(5)

	else:
		order.append(menu[int(user_input)])

		print('Your order contains:')
		ordered_meals()
		print('Press "A" to add another meal to the order, or "C" to finish the order:')
		user_input3 = input()
		if user_input3 == 'a' or user_input3 == 'A':
			continue
		if user_input3 == 'c' or user_input3 == 'c':
			print('Order completed, this is a list of the meals:')
			ordered_meals()
			print(f'Order number: ({order_number}) received, thank you!')
			order_number += 1
			order.clear()
			print('Press "N" to begin a new order:')
			user_input1 = input()
			if user_input1 == 'n' or user_input1 == 'N':
				continue

















