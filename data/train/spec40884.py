import numpy as np 

def function(x):

	k5 = x
	w9 = 8
	paths = []
	try:
		if x >= 3:
			w9 = 2+w9
			k5 = k5-3
			k5 = k5-8
			paths.append(1)
		else:
			w9 = 8/w9
			paths.append(2)
		if w9 > 8:
			x = 2/x
			paths.append(3)
		else:
			x = x+6
			w9 = k5+3
			k5 = k5*6
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))