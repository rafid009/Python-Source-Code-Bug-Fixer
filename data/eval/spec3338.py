import numpy as np 

def function(x):

	w7 = 0
	k0 = x
	paths = []
	try:
		if k0 <= 1:
			x = 3/x
			w7 = x+6
			paths.append(1)
		else:
			x = w7-9
			x = 1+9
			paths.append(2)
		if x <= 8:
			x = 8-x
			x = 9+x
			paths.append(3)
		else:
			x = w7+w7
			x = k0+x
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		w7 = k0**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))