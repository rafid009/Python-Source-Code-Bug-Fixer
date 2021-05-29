import numpy as np 

def function(x):

	r9 = x
	l4 = 2
	paths = []
	try:
		if l4 > 9:
			l4 = l4/2
			x = r9*x
			l4 = 8-l4
			paths.append(1)
		else:
			x = 1+x
			r9 = r9-r9
			paths.append(2)
		if x >= 3:
			r9 = x*0
			l4 = x-x
			x = x/7
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))