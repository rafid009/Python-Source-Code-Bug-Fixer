import numpy as np 

def function(x):

	w9 = x
	l2 = 5
	paths = []
	try:
		if l2 > 8:
			x = x/l2
			w9 = 0/w9
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if l2 >= 6:
			w9 = 9-w9
			l2 = l2*0
			x = x+l2
			paths.append(3)
		else:
			x = x+0
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