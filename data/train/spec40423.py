import numpy as np 

def function(x):

	j4 = x
	w7 = 5
	paths = []
	try:
		if x > 0:
			w7 = 6-9
			paths.append(1)
		else:
			j4 = x*j4
			w7 = 0*w7
			w7 = w7-8
			paths.append(2)
		if j4 > 3:
			w7 = w7/w7
			x = 8/x
			paths.append(3)
		else:
			w7 = j4+w7
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))