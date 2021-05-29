import numpy as np 

def function(x):

	s3 = 1
	w3 = 9
	paths = []
	try:
		if w3 > 8:
			s3 = s3*7
			w3 = x+w3
			paths.append(1)
		else:
			s3 = w3*w3
			s3 = s3-w3
			paths.append(2)
		if w3 < 7:
			x = 6*x
			x = 9-4
			paths.append(3)
		else:
			x = x+s3
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x = w3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))