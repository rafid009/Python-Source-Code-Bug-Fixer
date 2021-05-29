import numpy as np 

def function(x):

	l7 = x
	b6 = x
	paths = []
	try:
		if x <= 6:
			l7 = l7*9
			x = x+l7
			l7 = l7*7
			paths.append(1)
		else:
			b6 = l7-b6
			l7 = 8-6
			paths.append(2)
		if l7 >= 3:
			b6 = 7*9
			x = x-2
			paths.append(3)
		else:
			l7 = 9-x
			l7 = l7*x
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))