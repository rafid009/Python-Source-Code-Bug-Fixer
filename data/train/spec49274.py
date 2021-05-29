import numpy as np 

def function(x):

	e5 = 4
	r6 = x
	paths = []
	try:
		if r6 >= 6:
			r6 = r6-0
			e5 = e5*1
			x = e5*8
			paths.append(1)
		else:
			e5 = r6+7
			paths.append(2)
		if r6 < 8:
			e5 = 7+e5
			e5 = r6/e5
			paths.append(3)
		else:
			x = x/5
			x = x-4
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