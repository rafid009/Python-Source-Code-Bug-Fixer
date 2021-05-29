import numpy as np 

def function(x):

	s5 = x
	p7 = x
	paths = []
	try:
		if x > 5:
			s5 = s5*3
			paths.append(1)
		else:
			p7 = x*p7
			s5 = s5+3
			paths.append(2)
		if p7 > 2:
			x = 2-x
			paths.append(3)
		else:
			p7 = 3/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p7 = x**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))