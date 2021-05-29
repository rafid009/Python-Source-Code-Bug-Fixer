import numpy as np 

def function(x):

	p2 = x
	s3 = 5
	paths = []
	try:
		if x > 1:
			p2 = x/5
			paths.append(1)
		else:
			p2 = p2+p2
			p2 = 8*p2
			paths.append(2)
		if s3 > 3:
			s3 = 2/x
			paths.append(3)
		else:
			p2 = p2+9
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))