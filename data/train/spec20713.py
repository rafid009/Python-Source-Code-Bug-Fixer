import numpy as np 

def function(x):

	w3 = x
	j4 = 0
	paths = []
	try:
		if w3 >= 7:
			x = 0+x
			w3 = 1+0
			x = 6-0
			paths.append(1)
		else:
			j4 = j4/w3
			j4 = x*j4
			paths.append(2)
		if j4 >= 9:
			j4 = j4+7
			x = 7/x
			x = 0-0
			paths.append(3)
		else:
			w3 = x-x
			j4 = x/5
			w3 = j4-2
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