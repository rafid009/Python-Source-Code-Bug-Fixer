import numpy as np 

def function(x):

	x6 = x
	i1 = 4
	paths = []
	try:
		if x6 >= 6:
			i1 = x+i1
			x = x/9
			x6 = i1-2
			paths.append(1)
		else:
			i1 = i1-9
			paths.append(2)
		if i1 >= 2:
			i1 = 0*i1
			x6 = x6/1
			x = 9/x
			paths.append(3)
		else:
			i1 = i1/i1
			x = 9+x
			i1 = i1/3
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