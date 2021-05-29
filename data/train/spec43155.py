import numpy as np 

def function(x):

	w3 = x
	k2 = x
	paths = []
	try:
		if x < 6:
			w3 = 1-w3
			paths.append(1)
		else:
			w3 = w3+7
			x = x+8
			x = x/7
			paths.append(2)
		if x < 5:
			k2 = k2*8
			k2 = k2+0
			paths.append(3)
		else:
			k2 = 2*k2
			x = w3+2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))