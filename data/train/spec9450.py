import numpy as np 

def function(x):

	w7 = 6
	k1 = x
	paths = []
	try:
		if x >= 7:
			x = x+w7
			w7 = w7/2
			w7 = 7+w7
			paths.append(1)
		else:
			w7 = 7+k1
			paths.append(2)
		if w7 >= 6:
			k1 = k1-2
			w7 = k1*w7
			x = x+7
			paths.append(3)
		else:
			x = x-0
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		k1 = w7**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))