import numpy as np 

def function(x):

	w7 = x
	x5 = x
	paths = []
	try:
		if x <= 1:
			w7 = 3*x
			w7 = x5*w7
			x = 7*2
			paths.append(1)
		else:
			x5 = x5-w7
			x = 8+x
			w7 = w7+1
			paths.append(2)
		if x > 4:
			w7 = w7/1
			paths.append(3)
		else:
			x5 = x5*6
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))