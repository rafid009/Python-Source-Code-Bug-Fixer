import numpy as np 

def function(x):

	r6 = 0
	s9 = x
	paths = []
	try:
		if s9 <= 0:
			s9 = 0+s9
			s9 = s9+r6
			r6 = r6/2
			paths.append(1)
		else:
			x = x*0
			r6 = r6-s9
			paths.append(2)
		if r6 < 3:
			r6 = s9*r6
			s9 = 4*s9
			x = x+6
			paths.append(3)
		else:
			s9 = 6*s9
			s9 = s9-s9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))