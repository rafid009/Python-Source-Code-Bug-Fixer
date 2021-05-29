import numpy as np 

def function(x):

	w6 = x
	q0 = 7
	paths = []
	try:
		if x > 3:
			x = x*9
			paths.append(1)
		else:
			q0 = 8/q0
			x = x/6
			paths.append(2)
		if q0 > 2:
			w6 = w6+4
			x = 6*3
			paths.append(3)
		else:
			w6 = q0-w6
			q0 = x+0
			w6 = 9/w6
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))