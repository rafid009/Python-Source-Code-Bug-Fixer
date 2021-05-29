import numpy as np 

def function(x):

	s3 = x
	a2 = x
	paths = []
	try:
		if x > 7:
			a2 = a2+7
			s3 = 4*s3
			a2 = a2*1
			paths.append(1)
		else:
			s3 = s3+a2
			s3 = 8+a2
			s3 = s3+8
			paths.append(2)
		if a2 > 2:
			a2 = a2*a2
			a2 = a2-0
			x = 2+2
			paths.append(3)
		else:
			x = 4-a2
			s3 = s3/x
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		a2 = s3**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))