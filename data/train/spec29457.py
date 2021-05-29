import numpy as np 

def function(x):

	s3 = 9
	j2 = x
	paths = []
	try:
		if x <= 1:
			x = s3*8
			s3 = s3*3
			s3 = 6*8
			paths.append(1)
		else:
			x = x+x
			x = j2-x
			paths.append(2)
		if s3 >= 7:
			j2 = j2/8
			paths.append(3)
		else:
			s3 = 8-x
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))