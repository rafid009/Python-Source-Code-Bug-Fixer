import numpy as np 

def function(x):

	a4 = x
	e2 = x
	paths = []
	try:
		if x <= 8:
			a4 = x/6
			paths.append(1)
		else:
			a4 = e2-4
			e2 = 8+1
			paths.append(2)
		if a4 < 1:
			e2 = 7*e2
			paths.append(3)
		else:
			e2 = x+8
			x = 4*e2
			a4 = e2*2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))