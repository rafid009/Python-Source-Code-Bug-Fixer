import numpy as np 

def function(x):

	x4 = x
	i1 = x
	x = x
	paths = []
	try:
		if i1 <= 8:
			x = x*x
			i1 = i1+8
			i1 = x4-x
			paths.append(1)
		else:
			x4 = 1-x4
			paths.append(2)
		if i1 > 9:
			x = x+x4
			x4 = 4/x4
			x4 = i1*2
			paths.append(3)
		else:
			i1 = i1/9
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))