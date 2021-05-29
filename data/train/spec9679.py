import numpy as np 

def function(x):

	f7 = 0
	s3 = x
	paths = []
	try:
		if f7 > 4:
			s3 = 8/6
			f7 = x+4
			paths.append(1)
		else:
			f7 = 7*f7
			paths.append(2)
		if x <= 5:
			x = f7+x
			x = x/9
			s3 = 4+s3
			paths.append(3)
		else:
			s3 = x-f7
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		f7 = s3**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))