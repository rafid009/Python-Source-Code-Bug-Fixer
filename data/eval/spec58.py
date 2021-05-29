import numpy as np 

def function(x):

	w7 = 8
	k7 = x
	paths = []
	try:
		if w7 > 8:
			x = x/8
			k7 = 0+8
			w7 = w7*w7
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if w7 >= 2:
			x = w7-3
			paths.append(3)
		else:
			x = k7*k7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))