import numpy as np 

def function(x):

	n6 = 0
	w8 = x
	paths = []
	try:
		if x <= 7:
			n6 = 1+n6
			x = 2+x
			paths.append(1)
		else:
			x = x*w8
			paths.append(2)
		if n6 >= 4:
			x = 4/x
			x = 7+x
			x = x/5
			paths.append(3)
		else:
			n6 = x-n6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))