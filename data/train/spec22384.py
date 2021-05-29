import numpy as np 

def function(x):

	r6 = x
	e7 = 8
	paths = []
	try:
		if r6 > 9:
			r6 = r6/8
			x = x+9
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if r6 >= 6:
			e7 = e7*4
			x = x-r6
			paths.append(3)
		else:
			r6 = r6-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))