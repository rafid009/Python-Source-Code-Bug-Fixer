import numpy as np 

def function(x):

	k1 = x
	w3 = 4
	paths = []
	try:
		if w3 <= 1:
			x = 8-x
			paths.append(1)
		else:
			k1 = k1*9
			x = w3-x
			x = x+2
			paths.append(2)
		if x > 2:
			x = x+1
			k1 = 4*w3
			k1 = k1-8
			paths.append(3)
		else:
			k1 = 0+k1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))