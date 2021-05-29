import numpy as np 

def function(x):

	z7 = x
	o9 = x
	paths = []
	try:
		if o9 > 5:
			x = x-x
			paths.append(1)
		else:
			x = 0/x
			x = x/5
			paths.append(2)
		if z7 <= 2:
			x = x-x
			paths.append(3)
		else:
			x = x+4
			x = x/3
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		z7 = o9**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))