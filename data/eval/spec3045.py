import numpy as np 

def function(x):

	w1 = 0
	k4 = x
	paths = []
	try:
		if w1 < 8:
			x = x/9
			x = x/3
			x = x-1
			paths.append(1)
		else:
			w1 = 2/w1
			paths.append(2)
		if k4 <= 3:
			w1 = w1-8
			paths.append(3)
		else:
			x = 5/x
			k4 = k4*8
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