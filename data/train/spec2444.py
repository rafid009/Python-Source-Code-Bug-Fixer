import numpy as np 

def function(x):

	e7 = 2
	a7 = x
	paths = []
	try:
		if e7 < 5:
			a7 = e7*a7
			e7 = e7/1
			e7 = e7/a7
			paths.append(1)
		else:
			e7 = 9-1
			paths.append(2)
		if a7 >= 7:
			e7 = e7*5
			x = 0/6
			paths.append(3)
		else:
			a7 = a7+1
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		a7 = e7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))