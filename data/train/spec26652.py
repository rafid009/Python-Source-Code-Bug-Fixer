import numpy as np 

def function(x):

	x3 = 8
	a2 = x
	paths = []
	try:
		if x3 >= 6:
			a2 = a2+6
			a2 = 8/a2
			x3 = a2*5
			paths.append(1)
		else:
			x3 = 8-x3
			a2 = a2*9
			paths.append(2)
		if x3 >= 0:
			a2 = x+7
			x = a2+x3
			x3 = x3-1
			paths.append(3)
		else:
			x3 = x3+3
			a2 = a2-8
			x3 = x3/3
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x3 = a2**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))