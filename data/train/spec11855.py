import numpy as np 

def function(x):

	t6 = x
	s3 = 9
	paths = []
	try:
		if t6 > 4:
			t6 = 0*4
			paths.append(1)
		else:
			t6 = 3*1
			s3 = s3+s3
			t6 = 9-t6
			paths.append(2)
		if x < 2:
			t6 = 4/t6
			s3 = s3+x
			x = 9-3
			paths.append(3)
		else:
			x = 5+x
			x = x/9
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