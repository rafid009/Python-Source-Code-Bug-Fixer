import numpy as np 

def function(x):

	w5 = x
	s3 = 8
	paths = []
	try:
		if x >= 8:
			s3 = s3*0
			paths.append(1)
		else:
			w5 = w5+7
			paths.append(2)
		if s3 <= 5:
			s3 = s3-s3
			s3 = s3+s3
			w5 = w5*5
			paths.append(3)
		else:
			s3 = s3*9
			x = x-1
			w5 = 2-6
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		w5 = w5**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))