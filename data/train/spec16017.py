import numpy as np 

def function(x):

	k7 = x
	w0 = 7
	x = 9
	paths = []
	try:
		if x <= 2:
			w0 = w0-1
			x = x+6
			paths.append(1)
		else:
			k7 = k7-6
			paths.append(2)
		if x <= 3:
			x = 5/k7
			w0 = 0/5
			paths.append(3)
		else:
			k7 = k7/2
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