import numpy as np 

def function(x):

	a3 = x
	e2 = x
	paths = []
	try:
		if e2 > 0:
			x = x+x
			a3 = a3-2
			paths.append(1)
		else:
			e2 = 0/e2
			paths.append(2)
		if x <= 9:
			x = 4/x
			e2 = 3+x
			paths.append(3)
		else:
			e2 = 0+1
			e2 = 3/e2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		a3 = e2**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))