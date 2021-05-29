import numpy as np 

def function(x):

	y1 = 1
	a2 = 1
	paths = []
	try:
		if y1 < 2:
			a2 = 4+x
			y1 = 8-a2
			paths.append(1)
		else:
			x = 6+9
			y1 = y1*5
			paths.append(2)
		if x >= 3:
			a2 = 4*a2
			paths.append(3)
		else:
			a2 = 2-7
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))