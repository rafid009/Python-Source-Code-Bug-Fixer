import numpy as np 

def function(x):

	e3 = 3
	r8 = x
	paths = []
	try:
		if x > 1:
			e3 = 3-x
			r8 = 6-r8
			x = r8*7
			paths.append(1)
		else:
			r8 = r8-x
			x = 1-r8
			paths.append(2)
		if e3 < 0:
			r8 = 2+r8
			r8 = r8*e3
			r8 = 0+r8
			paths.append(3)
		else:
			r8 = r8-x
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))