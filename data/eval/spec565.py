import numpy as np 

def function(x):

	p2 = 2
	s3 = x
	x = 8
	paths = []
	try:
		if x > 7:
			p2 = 0*p2
			p2 = x/1
			x = s3-3
			paths.append(1)
		else:
			p2 = p2*7
			s3 = 6*s3
			s3 = 3-x
			paths.append(2)
		if p2 <= 3:
			x = x*9
			x = p2/x
			paths.append(3)
		else:
			x = 2+x
			p2 = s3+8
			x = s3-p2
			paths.append(4)
		paths.append(5)
		assert s3 >= 0
		p2 = s3**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))