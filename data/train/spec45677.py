import numpy as np 

def function(x):

	k4 = 8
	w7 = 7
	paths = []
	try:
		if k4 > 8:
			w7 = 2-6
			k4 = 1*k4
			w7 = w7*k4
			paths.append(1)
		else:
			k4 = x+k4
			k4 = k4*9
			x = 9*w7
			paths.append(2)
		if x < 8:
			x = x*3
			x = 1-w7
			w7 = 9*w7
			paths.append(3)
		else:
			x = k4+x
			k4 = 9-k4
			w7 = w7-3
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k4 = k4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))