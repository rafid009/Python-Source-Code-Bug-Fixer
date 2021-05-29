import numpy as np 

def function(x):

	r1 = 1
	s6 = x
	paths = []
	try:
		if s6 > 4:
			r1 = 5+r1
			s6 = 1+s6
			s6 = s6-8
			paths.append(1)
		else:
			r1 = 0/r1
			s6 = r1+s6
			s6 = x*x
			paths.append(2)
		if s6 < 7:
			r1 = s6-x
			paths.append(3)
		else:
			x = x+5
			s6 = 4-9
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