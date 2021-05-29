import numpy as np 

def function(x):

	s4 = x
	p3 = 5
	paths = []
	try:
		if s4 < 8:
			p3 = p3/p3
			paths.append(1)
		else:
			s4 = s4/p3
			p3 = x-p3
			paths.append(2)
		if x >= 5:
			s4 = 4+2
			paths.append(3)
		else:
			s4 = s4+9
			p3 = 3+p3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))