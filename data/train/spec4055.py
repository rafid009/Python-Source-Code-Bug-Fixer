import numpy as np 

def function(x):

	j2 = 7
	s3 = x
	paths = []
	try:
		if x <= 2:
			x = 1+x
			x = x+7
			s3 = 0+7
			paths.append(1)
		else:
			j2 = 5-9
			s3 = 9+9
			x = x-s3
			paths.append(2)
		if j2 >= 6:
			s3 = j2+1
			s3 = s3/1
			j2 = s3+7
			paths.append(3)
		else:
			x = x/6
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s3 = x**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))