import numpy as np 

def function(x):

	s4 = 7
	p0 = 2
	x = x
	paths = []
	try:
		if x <= 4:
			x = 7/x
			s4 = s4-x
			x = x/2
			paths.append(1)
		else:
			s4 = 0-5
			paths.append(2)
		if p0 <= 6:
			s4 = 4+s4
			x = x/9
			paths.append(3)
		else:
			p0 = 2/x
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))