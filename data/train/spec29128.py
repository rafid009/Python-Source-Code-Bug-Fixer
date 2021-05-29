import numpy as np 

def function(x):

	r7 = x
	s3 = x
	x = x
	paths = []
	try:
		if x < 1:
			r7 = 7-r7
			s3 = 5*r7
			paths.append(1)
		else:
			s3 = 9*s3
			x = x/9
			x = 7-0
			paths.append(2)
		if x > 6:
			s3 = 2-s3
			x = 4/x
			x = x+3
			paths.append(3)
		else:
			r7 = x*0
			r7 = x+2
			r7 = s3*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))