import numpy as np 

def function(x):

	u2 = x
	l9 = 2
	paths = []
	try:
		if l9 >= 5:
			x = l9-x
			x = 5-x
			u2 = x+u2
			paths.append(1)
		else:
			u2 = u2*9
			paths.append(2)
		if l9 <= 8:
			u2 = u2-8
			paths.append(3)
		else:
			l9 = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))