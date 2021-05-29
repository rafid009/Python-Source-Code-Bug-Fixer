import numpy as np 

def function(x):

	e9 = 0
	a5 = x
	paths = []
	try:
		if a5 <= 3:
			e9 = e9+1
			e9 = 0-8
			paths.append(1)
		else:
			a5 = 1+a5
			e9 = 9+e9
			paths.append(2)
		if e9 <= 2:
			a5 = x/3
			paths.append(3)
		else:
			x = 0/x
			a5 = a5+9
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		e9 = a5**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))