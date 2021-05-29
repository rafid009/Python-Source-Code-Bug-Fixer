import numpy as np 

def function(x):

	p4 = 7
	s6 = 3
	paths = []
	try:
		if x <= 8:
			x = x*1
			paths.append(1)
		else:
			s6 = s6-x
			p4 = 7/x
			x = 0+x
			paths.append(2)
		if x > 7:
			s6 = 6*s6
			p4 = p4*3
			s6 = p4-6
			paths.append(3)
		else:
			p4 = 7/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))