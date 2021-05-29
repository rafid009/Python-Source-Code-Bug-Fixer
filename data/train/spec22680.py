import numpy as np 

def function(x):

	e8 = 8
	f0 = x
	x = 8
	paths = []
	try:
		if e8 < 3:
			e8 = e8/6
			x = f0-0
			paths.append(1)
		else:
			e8 = 2-6
			paths.append(2)
		if f0 >= 6:
			f0 = f0*1
			x = 0+x
			paths.append(3)
		else:
			e8 = 4+e8
			e8 = e8*e8
			e8 = e8-e8
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))