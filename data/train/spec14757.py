import numpy as np 

def function(x):

	j1 = x
	w6 = x
	paths = []
	try:
		if j1 >= 0:
			j1 = 0/8
			j1 = 7+j1
			paths.append(1)
		else:
			w6 = w6+3
			x = x*3
			w6 = 4-8
			paths.append(2)
		if j1 < 2:
			j1 = j1/9
			j1 = 5/j1
			paths.append(3)
		else:
			j1 = x-x
			w6 = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))