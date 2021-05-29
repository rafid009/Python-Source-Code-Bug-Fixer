import numpy as np 

def function(x):

	q0 = x
	f8 = 3
	paths = []
	try:
		if q0 < 1:
			f8 = f8*6
			x = f8/f8
			paths.append(1)
		else:
			q0 = 2+x
			paths.append(2)
		if q0 < 3:
			x = x+4
			f8 = f8-5
			f8 = f8*0
			paths.append(3)
		else:
			x = f8-x
			f8 = f8*6
			q0 = q0*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))