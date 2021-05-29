import numpy as np 

def function(x):

	b3 = x
	l9 = 7
	paths = []
	try:
		if b3 >= 3:
			l9 = l9-x
			x = l9*3
			paths.append(1)
		else:
			l9 = l9*l9
			l9 = b3-l9
			paths.append(2)
		if l9 >= 4:
			l9 = l9*l9
			l9 = l9*x
			l9 = x/8
			paths.append(3)
		else:
			l9 = l9*5
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		l9 = b3**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))