import numpy as np 

def function(x):

	e3 = x
	c6 = x
	paths = []
	try:
		if e3 <= 6:
			e3 = e3/4
			c6 = 0+c6
			paths.append(1)
		else:
			e3 = e3/e3
			e3 = e3*3
			e3 = e3-x
			paths.append(2)
		if e3 > 0:
			x = 2*0
			e3 = e3*6
			paths.append(3)
		else:
			x = x-6
			c6 = 3+c6
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