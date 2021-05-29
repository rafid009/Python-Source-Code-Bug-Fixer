import numpy as np 

def function(x):

	w6 = x
	n5 = x
	paths = []
	try:
		if n5 < 0:
			w6 = 1+w6
			w6 = 2-9
			w6 = w6+1
			paths.append(1)
		else:
			w6 = x*w6
			w6 = 1-0
			n5 = 6-n5
			paths.append(2)
		if x > 8:
			x = 7/x
			paths.append(3)
		else:
			n5 = n5/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))