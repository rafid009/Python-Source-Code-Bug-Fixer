import numpy as np 

def function(x):

	k2 = 0
	e4 = x
	x = x
	paths = []
	try:
		if x > 1:
			x = x-0
			paths.append(1)
		else:
			x = 5+9
			paths.append(2)
		if x <= 2:
			k2 = x+k2
			x = x+5
			paths.append(3)
		else:
			e4 = e4+9
			e4 = e4-9
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		k2 = e4**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))