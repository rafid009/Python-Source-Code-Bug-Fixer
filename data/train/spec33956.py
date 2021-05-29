import numpy as np 

def function(x):

	x5 = x
	w1 = 3
	paths = []
	try:
		if x >= 5:
			x = 8/x
			x = x+x5
			w1 = 6*3
			paths.append(1)
		else:
			w1 = x*w1
			x5 = 0+w1
			paths.append(2)
		if x5 > 6:
			x5 = x5*x5
			w1 = 8/w1
			w1 = w1*x5
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))