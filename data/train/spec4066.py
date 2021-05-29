import numpy as np 

def function(x):

	r6 = x
	s1 = x
	paths = []
	try:
		if s1 <= 2:
			r6 = r6*x
			r6 = r6*7
			paths.append(1)
		else:
			s1 = s1+3
			s1 = s1+s1
			paths.append(2)
		if s1 > 6:
			r6 = r6+7
			x = 6-0
			paths.append(3)
		else:
			r6 = r6/r6
			r6 = 0*3
			s1 = s1-s1
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