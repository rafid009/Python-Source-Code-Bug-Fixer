import numpy as np 

def function(x):

	e9 = 1
	a3 = x
	paths = []
	try:
		if a3 < 6:
			e9 = e9-2
			a3 = 8+3
			a3 = a3+6
			paths.append(1)
		else:
			e9 = e9+x
			paths.append(2)
		if e9 <= 9:
			a3 = 2-e9
			paths.append(3)
		else:
			a3 = a3+a3
			a3 = 8+a3
			e9 = e9-7
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))