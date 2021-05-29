import numpy as np 

def function(x):

	r6 = x
	s7 = x
	paths = []
	try:
		if s7 > 4:
			s7 = 8-s7
			x = x-3
			s7 = 7*s7
			paths.append(1)
		else:
			s7 = s7-x
			paths.append(2)
		if s7 > 6:
			x = x/2
			paths.append(3)
		else:
			s7 = 6*s7
			r6 = r6/7
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		r6 = r6**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))