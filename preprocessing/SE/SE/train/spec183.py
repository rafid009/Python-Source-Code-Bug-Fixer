import numpy as np 

def function(x):

	a9 = x
	y4 = 6
	paths = []
	try:
		if a9 > 1:
			x = x+x
			y4 = 6+y4
			paths.append(1)
		else:
			a9 = 9-a9
			x = x-5
			paths.append(2)
		if x >= 9:
			x = 8+x
			a9 = a9-x
			x = 6-2
			paths.append(3)
		else:
			x = a9*5
			a9 = 8*3
			y4 = y4*x
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))