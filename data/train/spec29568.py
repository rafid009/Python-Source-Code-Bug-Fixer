import numpy as np 

def function(x):

	l9 = x
	b5 = x
	paths = []
	try:
		if b5 <= 6:
			x = 5/x
			paths.append(1)
		else:
			b5 = b5*3
			paths.append(2)
		if b5 < 1:
			l9 = l9/5
			paths.append(3)
		else:
			l9 = l9*5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		l9 = b5**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))