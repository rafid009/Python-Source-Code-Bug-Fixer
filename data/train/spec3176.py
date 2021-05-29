import numpy as np 

def function(x):

	l4 = 8
	v7 = 1
	paths = []
	try:
		if v7 <= 9:
			x = 6+x
			paths.append(1)
		else:
			l4 = 6+x
			paths.append(2)
		if l4 >= 6:
			x = x*7
			paths.append(3)
		else:
			l4 = 4+6
			l4 = l4/6
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))