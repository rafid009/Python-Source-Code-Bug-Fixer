import numpy as np 

def function(x):

	n7 = 1
	w5 = x
	paths = []
	try:
		if x >= 3:
			x = x*x
			x = 1-x
			w5 = w5+7
			paths.append(1)
		else:
			w5 = w5+0
			x = 4/x
			paths.append(2)
		if w5 >= 5:
			w5 = 4*w5
			w5 = w5-n7
			n7 = 4*n7
			paths.append(3)
		else:
			n7 = 9/n7
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))