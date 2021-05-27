import numpy as np 

def function(x):

	w1 = 9
	i1 = 8
	paths = []
	try:
		if w1 < 5:
			i1 = i1/w1
			paths.append(1)
		else:
			i1 = 7+i1
			w1 = w1-x
			i1 = 3*i1
			paths.append(2)
		if i1 < 3:
			x = 4/x
			i1 = i1/w1
			paths.append(3)
		else:
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))