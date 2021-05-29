import numpy as np 

def function(x):

	k1 = 0
	w8 = 3
	paths = []
	try:
		if k1 > 6:
			x = 4/x
			paths.append(1)
		else:
			w8 = w8/x
			paths.append(2)
		if x > 4:
			w8 = x-3
			x = w8-x
			paths.append(3)
		else:
			x = 1+x
			k1 = k1+3
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		k1 = w8**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))