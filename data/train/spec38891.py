import numpy as np 

def function(x):

	e6 = x
	x2 = 8
	paths = []
	try:
		if e6 >= 5:
			x2 = 7-2
			x = x2+x
			x2 = x2-8
			paths.append(1)
		else:
			x2 = x2*e6
			x2 = x2/9
			e6 = 0+8
			paths.append(2)
		if x2 >= 8:
			x = x-8
			x = e6/x2
			x2 = e6*2
			paths.append(3)
		else:
			e6 = e6*9
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		e6 = x2**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))