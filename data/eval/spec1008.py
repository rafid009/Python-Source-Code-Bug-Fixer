import numpy as np 

def function(x):

	j1 = 2
	w8 = 3
	paths = []
	try:
		if x >= 7:
			j1 = 7/3
			j1 = w8*j1
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if x < 4:
			w8 = 6/w8
			j1 = j1-j1
			paths.append(3)
		else:
			x = x-x
			j1 = 0*x
			j1 = j1-6
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))