import numpy as np 

def function(x):

	w3 = x
	k2 = 0
	paths = []
	try:
		if k2 <= 3:
			k2 = k2+3
			w3 = w3+6
			paths.append(1)
		else:
			k2 = w3/k2
			k2 = w3/k2
			k2 = w3-x
			paths.append(2)
		if x >= 4:
			x = 4-x
			w3 = w3+x
			x = x*2
			paths.append(3)
		else:
			x = x+9
			k2 = k2*6
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))