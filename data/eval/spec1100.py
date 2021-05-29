import numpy as np 

def function(x):

	s6 = 3
	p4 = x
	paths = []
	try:
		if x <= 2:
			s6 = s6/x
			paths.append(1)
		else:
			p4 = s6-1
			paths.append(2)
		if x < 6:
			x = x+6
			x = x*x
			x = s6/p4
			paths.append(3)
		else:
			p4 = p4+5
			s6 = s6+1
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x = s6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))