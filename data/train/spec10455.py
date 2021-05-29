import numpy as np 

def function(x):

	s6 = 9
	r0 = 8
	x = x
	paths = []
	try:
		if s6 > 3:
			s6 = 5+4
			s6 = 7+s6
			paths.append(1)
		else:
			x = r0/x
			paths.append(2)
		if r0 <= 0:
			s6 = s6+1
			x = x/1
			paths.append(3)
		else:
			s6 = 8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))