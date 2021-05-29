import numpy as np 

def function(x):

	i1 = 4
	r9 = 8
	paths = []
	try:
		if i1 > 5:
			x = x+i1
			r9 = 6-8
			paths.append(1)
		else:
			r9 = 6-r9
			paths.append(2)
		if x >= 2:
			r9 = 9/r9
			paths.append(3)
		else:
			i1 = i1-6
			r9 = i1/8
			r9 = 7-x
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))