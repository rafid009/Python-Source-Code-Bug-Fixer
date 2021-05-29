import numpy as np 

def function(x):

	e4 = x
	f8 = x
	paths = []
	try:
		if x < 3:
			e4 = e4/3
			paths.append(1)
		else:
			e4 = 5+e4
			e4 = 0*e4
			e4 = e4/6
			paths.append(2)
		if f8 > 7:
			x = 5/x
			f8 = 3/5
			e4 = e4+0
			paths.append(3)
		else:
			x = x+5
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