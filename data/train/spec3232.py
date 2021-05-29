import numpy as np 

def function(x):

	e3 = 9
	s3 = 3
	paths = []
	try:
		if e3 > 1:
			x = x-1
			paths.append(1)
		else:
			s3 = 7+x
			s3 = 1/2
			paths.append(2)
		if e3 >= 7:
			x = 4-x
			paths.append(3)
		else:
			e3 = e3+s3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))