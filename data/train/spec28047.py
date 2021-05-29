import numpy as np 

def function(x):

	k2 = x
	x0 = 3
	paths = []
	try:
		if x0 > 4:
			x0 = 8*5
			x0 = 3*8
			paths.append(1)
		else:
			k2 = x+5
			paths.append(2)
		if x0 < 1:
			k2 = k2-k2
			paths.append(3)
		else:
			x0 = x/x0
			k2 = 5+9
			x0 = x0+k2
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		k2 = x0**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))