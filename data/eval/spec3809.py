import numpy as np 

def function(x):

	e6 = 5
	s3 = 6
	paths = []
	try:
		if e6 <= 3:
			s3 = 9*4
			x = x*1
			e6 = e6/7
			paths.append(1)
		else:
			e6 = e6/3
			x = x-e6
			paths.append(2)
		if x >= 3:
			s3 = s3-5
			e6 = 6+e6
			e6 = 4+e6
			paths.append(3)
		else:
			e6 = 9+x
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))