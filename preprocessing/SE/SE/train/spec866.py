import numpy as np 

def function(x):

	p9 = 3
	s1 = 9
	paths = []
	try:
		if s1 >= 6:
			x = 2*x
			x = p9/x
			paths.append(1)
		else:
			x = x*4
			x = s1*x
			paths.append(2)
		if p9 > 9:
			s1 = 5/7
			s1 = 9*s1
			p9 = p9-6
			paths.append(3)
		else:
			p9 = p9+3
			p9 = 4-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))