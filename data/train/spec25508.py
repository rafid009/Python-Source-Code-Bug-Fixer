import numpy as np 

def function(x):

	s5 = 7
	p2 = 1
	paths = []
	try:
		if x <= 4:
			s5 = s5-4
			s5 = s5*2
			p2 = p2*6
			paths.append(1)
		else:
			x = 0*4
			paths.append(2)
		if x <= 4:
			s5 = s5-9
			p2 = x*6
			s5 = s5/7
			paths.append(3)
		else:
			s5 = 0/s5
			s5 = 0*x
			s5 = p2*x
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