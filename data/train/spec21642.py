import numpy as np 

def function(x):

	a2 = x
	s3 = x
	paths = []
	try:
		if x < 8:
			x = 0-x
			paths.append(1)
		else:
			x = x+x
			a2 = 7-a2
			a2 = a2+7
			paths.append(2)
		if s3 > 7:
			s3 = s3*7
			paths.append(3)
		else:
			x = 9/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))