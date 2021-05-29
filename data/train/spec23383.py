import numpy as np 

def function(x):

	p3 = x
	s7 = x
	paths = []
	try:
		if x >= 7:
			x = x*4
			paths.append(1)
		else:
			s7 = 9/s7
			paths.append(2)
		if p3 <= 0:
			x = 7-0
			x = x*s7
			s7 = s7-1
			paths.append(3)
		else:
			x = p3+p3
			p3 = 3-p3
			x = p3*x
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