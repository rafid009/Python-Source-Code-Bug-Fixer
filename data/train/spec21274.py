import numpy as np 

def function(x):

	s7 = 0
	p6 = x
	paths = []
	try:
		if p6 >= 8:
			x = x+s7
			paths.append(1)
		else:
			s7 = 0/1
			p6 = p6-s7
			x = x/2
			paths.append(2)
		if s7 <= 6:
			p6 = 0-p6
			paths.append(3)
		else:
			p6 = p6*x
			x = x*6
			s7 = 4/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))