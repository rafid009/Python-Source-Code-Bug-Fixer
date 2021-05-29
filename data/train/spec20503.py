import numpy as np 

def function(x):

	a7 = x
	y5 = x
	paths = []
	try:
		if a7 < 7:
			y5 = x*y5
			a7 = a7*9
			a7 = a7+8
			paths.append(1)
		else:
			y5 = 2-y5
			a7 = 3-y5
			paths.append(2)
		if a7 >= 3:
			y5 = y5*2
			paths.append(3)
		else:
			y5 = a7*a7
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		a7 = y5**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))