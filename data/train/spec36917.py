import numpy as np 

def function(x):

	q8 = 9
	a7 = x
	paths = []
	try:
		if x > 9:
			q8 = 2*q8
			paths.append(1)
		else:
			a7 = a7/a7
			x = x-a7
			a7 = x/a7
			paths.append(2)
		if x >= 3:
			q8 = 9-q8
			paths.append(3)
		else:
			x = a7+9
			x = x+1
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		a7 = q8**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))