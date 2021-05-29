import numpy as np 

def function(x):

	w7 = 4
	j7 = 8
	paths = []
	try:
		if x > 5:
			w7 = 1*w7
			paths.append(1)
		else:
			w7 = w7-w7
			x = 8/x
			w7 = w7*j7
			paths.append(2)
		if j7 < 0:
			j7 = j7*1
			w7 = w7/2
			paths.append(3)
		else:
			w7 = w7+j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w7 = x**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))