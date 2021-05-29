import numpy as np 

def function(x):

	k4 = x
	w8 = x
	paths = []
	try:
		if k4 >= 2:
			w8 = w8-8
			k4 = x+k4
			paths.append(1)
		else:
			w8 = x-8
			k4 = x/9
			paths.append(2)
		if x > 7:
			w8 = 1/w8
			paths.append(3)
		else:
			x = x/8
			x = 5+6
			k4 = k4*1
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))