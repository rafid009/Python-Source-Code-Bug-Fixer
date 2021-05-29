import numpy as np 

def function(x):

	e0 = x
	x6 = x
	paths = []
	try:
		if e0 >= 6:
			x = 4/2
			e0 = 5+e0
			e0 = e0+x6
			paths.append(1)
		else:
			e0 = 1-4
			paths.append(2)
		if x >= 4:
			x = 6-x
			x = 6-x6
			paths.append(3)
		else:
			e0 = e0*0
			x = x6-e0
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		e0 = e0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))