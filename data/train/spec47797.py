import numpy as np 

def function(x):

	e4 = x
	f0 = 9
	paths = []
	try:
		if e4 >= 0:
			e4 = x-4
			e4 = e4-f0
			paths.append(1)
		else:
			f0 = 0/8
			x = x+x
			paths.append(2)
		if f0 > 9:
			x = 4/x
			e4 = e4-e4
			f0 = x-f0
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))