import numpy as np 

def function(x):

	a7 = x
	i1 = x
	paths = []
	try:
		if x > 5:
			x = 6-1
			paths.append(1)
		else:
			i1 = i1/i1
			x = 1*a7
			paths.append(2)
		if x >= 5:
			i1 = 8/3
			paths.append(3)
		else:
			i1 = i1/a7
			i1 = i1+x
			x = x*2
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))