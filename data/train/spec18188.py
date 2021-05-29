import numpy as np 

def function(x):

	u3 = x
	s3 = 6
	x = x
	paths = []
	try:
		if u3 > 9:
			s3 = s3/2
			s3 = s3/s3
			paths.append(1)
		else:
			s3 = s3*u3
			x = x*0
			u3 = u3*1
			paths.append(2)
		if u3 < 2:
			x = x/4
			paths.append(3)
		else:
			s3 = s3-s3
			u3 = u3+s3
			u3 = u3-4
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		s3 = u3**0.5
		return s3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))