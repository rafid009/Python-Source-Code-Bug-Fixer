import numpy as np 

def function(x):

	f4 = x
	e2 = 8
	x = 0
	paths = []
	try:
		if e2 <= 3:
			f4 = 1/x
			paths.append(1)
		else:
			e2 = x*4
			paths.append(2)
		if e2 < 1:
			e2 = e2/1
			f4 = f4+9
			paths.append(3)
		else:
			e2 = 8/x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		e2 = f4**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))