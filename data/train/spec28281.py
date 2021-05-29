import numpy as np 

def function(x):

	v7 = x
	a4 = 4
	paths = []
	try:
		if a4 > 4:
			a4 = a4-v7
			v7 = v7*6
			x = x+x
			paths.append(1)
		else:
			a4 = a4+a4
			v7 = a4+a4
			a4 = a4*1
			paths.append(2)
		if v7 > 3:
			v7 = 2/3
			x = x-2
			a4 = x-a4
			paths.append(3)
		else:
			a4 = a4+9
			v7 = v7-4
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