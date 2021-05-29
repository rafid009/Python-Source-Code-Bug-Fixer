import numpy as np 

def function(x):

	x0 = x
	w6 = x
	paths = []
	try:
		if x0 > 7:
			x0 = x0*0
			x = w6+x
			x0 = x0-6
			paths.append(1)
		else:
			x0 = 7/x0
			paths.append(2)
		if w6 >= 7:
			x = x*6
			x = 2+x
			x = x0-0
			paths.append(3)
		else:
			x = x0*w6
			x0 = x0*3
			w6 = w6/2
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x = x0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))