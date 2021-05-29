import numpy as np 

def function(x):

	e7 = 3
	a5 = x
	paths = []
	try:
		if a5 <= 6:
			a5 = x+a5
			x = x/2
			x = x*8
			paths.append(1)
		else:
			a5 = a5/a5
			e7 = e7+5
			paths.append(2)
		if a5 > 3:
			x = x-3
			e7 = 7+e7
			paths.append(3)
		else:
			x = x*8
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))