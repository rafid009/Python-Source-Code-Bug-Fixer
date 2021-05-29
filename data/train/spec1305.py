import numpy as np 

def function(x):

	r3 = x
	e5 = 9
	paths = []
	try:
		if e5 <= 3:
			e5 = 6-1
			r3 = 4-2
			paths.append(1)
		else:
			r3 = 4+5
			paths.append(2)
		if e5 >= 3:
			x = r3-x
			paths.append(3)
		else:
			x = 4/e5
			r3 = 5/6
			r3 = 5+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))