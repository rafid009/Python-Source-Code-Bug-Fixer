import numpy as np 

def function(x):

	s0 = x
	n2 = 5
	paths = []
	try:
		if s0 > 0:
			s0 = s0*1
			x = x*s0
			paths.append(1)
		else:
			x = x+6
			paths.append(2)
		if n2 < 9:
			s0 = 5-s0
			paths.append(3)
		else:
			n2 = n2-6
			n2 = n2*0
			s0 = 5*s0
			paths.append(4)
		paths.append(5)
		assert s0 >= 0
		n2 = s0**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))