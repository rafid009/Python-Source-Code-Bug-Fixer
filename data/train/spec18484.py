import numpy as np 

def function(x):

	s3 = x
	i1 = x
	x = 1
	paths = []
	try:
		if s3 > 2:
			s3 = x+s3
			x = 7-0
			x = x/9
			paths.append(1)
		else:
			x = 4-i1
			paths.append(2)
		if i1 >= 3:
			s3 = 1*s3
			s3 = s3/x
			i1 = 8+i1
			paths.append(3)
		else:
			x = 5/8
			x = x/5
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))