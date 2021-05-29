import numpy as np 

def function(x):

	s3 = 7
	r7 = x
	paths = []
	try:
		if r7 < 6:
			x = r7-9
			x = x-2
			paths.append(1)
		else:
			r7 = 9+r7
			paths.append(2)
		if x > 7:
			x = r7/x
			x = s3*x
			r7 = r7+r7
			paths.append(3)
		else:
			r7 = 1*0
			s3 = r7+1
			s3 = x+7
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