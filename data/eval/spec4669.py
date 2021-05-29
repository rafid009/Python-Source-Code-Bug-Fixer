import numpy as np 

def function(x):

	i1 = 7
	e9 = x
	x = x
	paths = []
	try:
		if i1 > 2:
			e9 = 2*i1
			paths.append(1)
		else:
			x = x*3
			e9 = e9-i1
			paths.append(2)
		if x <= 3:
			x = x-5
			e9 = e9*1
			paths.append(3)
		else:
			i1 = 8-x
			e9 = 2+2
			x = 4*x
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