import numpy as np 

def function(x):

	s6 = 1
	r3 = x
	paths = []
	try:
		if s6 < 5:
			s6 = s6*s6
			paths.append(1)
		else:
			s6 = 6+s6
			paths.append(2)
		if r3 > 4:
			r3 = r3+3
			s6 = x+s6
			paths.append(3)
		else:
			x = x+r3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))