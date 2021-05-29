import numpy as np 

def function(x):

	a1 = x
	e7 = x
	x = x
	paths = []
	try:
		if e7 < 5:
			e7 = 6/e7
			e7 = 4+a1
			paths.append(1)
		else:
			a1 = a1-0
			paths.append(2)
		if a1 < 0:
			e7 = e7*5
			paths.append(3)
		else:
			x = x*5
			a1 = a1+1
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		a1 = e7**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))