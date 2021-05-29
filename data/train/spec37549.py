import numpy as np 

def function(x):

	r4 = 0
	e9 = x
	x = 4
	paths = []
	try:
		if e9 <= 8:
			x = 6*r4
			x = x*x
			paths.append(1)
		else:
			r4 = r4+e9
			paths.append(2)
		if e9 < 4:
			r4 = 8-r4
			x = 9-x
			paths.append(3)
		else:
			e9 = e9-2
			r4 = x-r4
			x = x*x
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))