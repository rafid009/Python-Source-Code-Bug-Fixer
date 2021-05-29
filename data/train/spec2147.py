import numpy as np 

def function(x):

	s3 = x
	u8 = x
	paths = []
	try:
		if s3 <= 0:
			s3 = s3-6
			u8 = u8*2
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if s3 <= 5:
			x = 2*0
			paths.append(3)
		else:
			x = x*6
			x = x-x
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