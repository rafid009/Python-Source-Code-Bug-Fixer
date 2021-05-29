import numpy as np 

def function(x):

	w6 = 6
	k2 = 3
	paths = []
	try:
		if x < 5:
			x = 9+7
			x = k2/1
			paths.append(1)
		else:
			w6 = w6+w6
			w6 = 6*w6
			paths.append(2)
		if x < 3:
			w6 = w6/k2
			x = 9+x
			paths.append(3)
		else:
			k2 = k2/3
			x = x-w6
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