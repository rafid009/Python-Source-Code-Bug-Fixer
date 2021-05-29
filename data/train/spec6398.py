import numpy as np 

def function(x):

	s7 = 9
	p4 = 2
	paths = []
	try:
		if p4 < 4:
			x = x/p4
			paths.append(1)
		else:
			x = x-x
			p4 = p4*2
			x = x+p4
			paths.append(2)
		if x > 0:
			p4 = p4-2
			p4 = p4*7
			s7 = s7*7
			paths.append(3)
		else:
			p4 = 5/7
			s7 = 2*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p4 = x**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))