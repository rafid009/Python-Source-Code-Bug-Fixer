import numpy as np 

def function(x):

	j3 = x
	w7 = 3
	paths = []
	try:
		if w7 >= 1:
			w7 = 6/1
			w7 = x*w7
			x = 7-x
			paths.append(1)
		else:
			w7 = 0/x
			j3 = j3*5
			w7 = w7-4
			paths.append(2)
		if x >= 5:
			j3 = 5*x
			paths.append(3)
		else:
			j3 = 5*w7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))