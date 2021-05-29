import numpy as np 

def function(x):

	s0 = x
	p3 = 9
	paths = []
	try:
		if p3 >= 4:
			s0 = x*5
			paths.append(1)
		else:
			s0 = 2/p3
			paths.append(2)
		if p3 > 8:
			p3 = p3+6
			p3 = p3*5
			paths.append(3)
		else:
			p3 = p3*1
			p3 = 4+p3
			p3 = 3*p3
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		p3 = s0**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))