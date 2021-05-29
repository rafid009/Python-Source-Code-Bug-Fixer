import numpy as np 

def function(x):

	p1 = x
	s3 = x
	paths = []
	try:
		if p1 >= 5:
			p1 = p1/x
			paths.append(1)
		else:
			p1 = 9-2
			paths.append(2)
		if s3 >= 9:
			x = x*x
			paths.append(3)
		else:
			p1 = 0+s3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))