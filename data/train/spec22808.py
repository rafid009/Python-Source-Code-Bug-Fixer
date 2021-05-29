import numpy as np 

def function(x):

	r5 = 8
	x7 = 8
	paths = []
	try:
		if r5 >= 1:
			r5 = r5-r5
			r5 = 7*0
			paths.append(1)
		else:
			r5 = r5+7
			x7 = 3*x7
			paths.append(2)
		if r5 >= 4:
			x = 4/x
			paths.append(3)
		else:
			x7 = 8+8
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