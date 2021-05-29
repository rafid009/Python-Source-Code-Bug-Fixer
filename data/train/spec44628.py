import numpy as np 

def function(x):

	i2 = x
	w7 = x
	paths = []
	try:
		if x <= 4:
			w7 = w7/w7
			paths.append(1)
		else:
			x = 4*w7
			x = 8/7
			paths.append(2)
		if x <= 1:
			w7 = 8-i2
			x = x*3
			paths.append(3)
		else:
			w7 = 3+w7
			w7 = w7/8
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		w7 = i2**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))