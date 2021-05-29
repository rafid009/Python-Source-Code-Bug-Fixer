import numpy as np 

def function(x):

	p2 = 0
	s8 = 2
	x = x
	paths = []
	try:
		if x >= 8:
			x = x-2
			p2 = 4*p2
			p2 = 8+p2
			paths.append(1)
		else:
			x = 9+x
			x = s8*x
			x = 8/x
			paths.append(2)
		if s8 < 8:
			x = x*9
			paths.append(3)
		else:
			x = x+s8
			x = 1-x
			s8 = s8*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))