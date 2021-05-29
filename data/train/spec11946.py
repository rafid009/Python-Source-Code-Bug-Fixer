import numpy as np 

def function(x):

	n4 = x
	f3 = x
	paths = []
	try:
		if n4 <= 9:
			x = x*4
			x = x/4
			n4 = n4-3
			paths.append(1)
		else:
			x = 6/x
			n4 = 9-x
			f3 = 3-2
			paths.append(2)
		if n4 < 7:
			f3 = f3+f3
			x = x+9
			paths.append(3)
		else:
			x = x+9
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