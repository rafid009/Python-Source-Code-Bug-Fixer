import numpy as np 

def function(x):

	s7 = 3
	p4 = x
	paths = []
	try:
		if p4 <= 8:
			s7 = 0-s7
			p4 = p4-8
			paths.append(1)
		else:
			p4 = 4*3
			x = 3/x
			paths.append(2)
		if p4 <= 1:
			x = x*1
			paths.append(3)
		else:
			x = x/p4
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		p4 = s7**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))