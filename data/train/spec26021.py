import numpy as np 

def function(x):

	s3 = x
	b5 = x
	x = 1
	paths = []
	try:
		if b5 < 4:
			b5 = b5+5
			x = 5+8
			b5 = 1-9
			paths.append(1)
		else:
			b5 = b5+6
			b5 = b5-8
			b5 = 2+s3
			paths.append(2)
		if b5 < 4:
			x = 4+s3
			s3 = x/5
			x = 4/b5
			paths.append(3)
		else:
			x = x+6
			x = b5*x
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		b5 = s3**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))