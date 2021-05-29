import numpy as np 

def function(x):

	e0 = 0
	f7 = x
	x = 7
	paths = []
	try:
		if x > 9:
			f7 = f7+3
			paths.append(1)
		else:
			f7 = f7*9
			paths.append(2)
		if e0 >= 3:
			x = x-e0
			x = x+4
			f7 = 7-f7
			paths.append(3)
		else:
			e0 = x+e0
			f7 = x-8
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		e0 = f7**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))