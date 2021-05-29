import numpy as np 

def function(x):

	a3 = 7
	e2 = x
	paths = []
	try:
		if e2 <= 6:
			a3 = a3+6
			x = x+9
			paths.append(1)
		else:
			x = 6-x
			paths.append(2)
		if e2 < 2:
			e2 = e2-a3
			a3 = a3/e2
			x = x+x
			paths.append(3)
		else:
			e2 = e2+6
			x = e2-9
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