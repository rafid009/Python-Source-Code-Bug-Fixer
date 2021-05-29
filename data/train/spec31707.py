import numpy as np 

def function(x):

	r9 = x
	e3 = 7
	paths = []
	try:
		if e3 <= 4:
			x = x-1
			paths.append(1)
		else:
			e3 = 4-e3
			e3 = e3/1
			paths.append(2)
		if r9 <= 8:
			r9 = r9/2
			x = r9/x
			paths.append(3)
		else:
			r9 = 3/r9
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		r9 = e3**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))