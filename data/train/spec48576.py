import numpy as np 

def function(x):

	p2 = 0
	s2 = 6
	paths = []
	try:
		if x <= 7:
			x = 7+x
			p2 = p2+7
			paths.append(1)
		else:
			s2 = 4/s2
			s2 = 1-x
			paths.append(2)
		if s2 >= 6:
			p2 = 4-p2
			s2 = s2+7
			paths.append(3)
		else:
			x = x*p2
			x = 0*p2
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		p2 = s2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))