import numpy as np 

def function(x):

	o1 = x
	e6 = 9
	paths = []
	try:
		if e6 > 8:
			e6 = 1-o1
			e6 = x-5
			x = x*x
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if o1 <= 8:
			o1 = o1+8
			paths.append(3)
		else:
			o1 = 9-o1
			e6 = e6/e6
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		x = e6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))