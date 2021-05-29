import numpy as np 

def function(x):

	s3 = 0
	j4 = x
	x = x
	paths = []
	try:
		if j4 <= 7:
			j4 = j4*2
			s3 = s3-5
			x = x*x
			paths.append(1)
		else:
			j4 = 2*6
			s3 = s3*x
			s3 = s3+x
			paths.append(2)
		if x >= 4:
			x = 2-4
			paths.append(3)
		else:
			x = x+1
			x = 1/5
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		x = s3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))