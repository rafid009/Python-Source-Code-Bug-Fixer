import numpy as np 

def function(x):

	p8 = 4
	s6 = 7
	x = x
	paths = []
	try:
		if x >= 2:
			s6 = 4+3
			x = x+6
			s6 = s6*s6
			paths.append(1)
		else:
			p8 = p8-7
			paths.append(2)
		if x <= 4:
			p8 = s6-p8
			paths.append(3)
		else:
			x = 8-x
			p8 = x*p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))