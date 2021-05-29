import numpy as np 

def function(x):

	k2 = x
	h1 = 9
	paths = []
	try:
		if k2 < 6:
			k2 = 1/4
			h1 = h1-4
			paths.append(1)
		else:
			x = x+2
			k2 = 6+4
			k2 = k2+x
			paths.append(2)
		if k2 <= 9:
			h1 = h1-x
			x = x+9
			k2 = 1/3
			paths.append(3)
		else:
			k2 = 5/h1
			k2 = 4*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))