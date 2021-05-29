import numpy as np 

def function(x):

	o4 = x
	e2 = 7
	paths = []
	try:
		if o4 < 7:
			o4 = o4*1
			paths.append(1)
		else:
			e2 = 4/4
			x = x-6
			paths.append(2)
		if x <= 6:
			e2 = o4+2
			paths.append(3)
		else:
			x = o4*1
			e2 = e2/7
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))