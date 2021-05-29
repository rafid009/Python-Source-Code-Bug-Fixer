import numpy as np 

def function(x):

	i9 = 4
	v7 = 8
	paths = []
	try:
		if i9 < 3:
			v7 = i9/8
			i9 = i9*8
			paths.append(1)
		else:
			v7 = v7-9
			x = x*5
			paths.append(2)
		if v7 >= 5:
			x = 6*6
			x = x+x
			i9 = 1*x
			paths.append(3)
		else:
			v7 = v7/6
			v7 = v7/x
			v7 = 5*1
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