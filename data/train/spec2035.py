import numpy as np 

def function(x):

	w1 = x
	x0 = x
	x = 8
	paths = []
	try:
		if w1 < 1:
			x0 = x0-4
			x = x*8
			w1 = 3/x0
			paths.append(1)
		else:
			x0 = x0-4
			x = x*x
			x0 = w1-0
			paths.append(2)
		if x0 < 9:
			w1 = 4-w1
			w1 = w1*8
			x0 = x*5
			paths.append(3)
		else:
			x0 = w1*0
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x0 = w1**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))