import numpy as np 

def function(x):

	g3 = x
	s3 = x
	paths = []
	try:
		if g3 >= 4:
			x = 9/s3
			x = x*s3
			g3 = x-0
			paths.append(1)
		else:
			x = 1/7
			s3 = g3/g3
			paths.append(2)
		if g3 >= 1:
			g3 = g3/5
			x = 8+x
			paths.append(3)
		else:
			x = x+g3
			g3 = g3+s3
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		s3 = g3**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))