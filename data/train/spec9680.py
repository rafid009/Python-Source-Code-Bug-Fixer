import numpy as np 

def function(x):

	l4 = x
	r2 = 9
	paths = []
	try:
		if x > 5:
			x = 7*4
			x = 1*x
			paths.append(1)
		else:
			l4 = l4/3
			x = x-l4
			x = 7+x
			paths.append(2)
		if x >= 5:
			x = x-x
			x = x+x
			paths.append(3)
		else:
			x = 7-r2
			l4 = x-2
			x = l4*2
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