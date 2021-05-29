import numpy as np 

def function(x):

	r5 = x
	s9 = 7
	paths = []
	try:
		if x >= 6:
			s9 = s9-8
			s9 = 4/s9
			x = x*3
			paths.append(1)
		else:
			r5 = r5*x
			r5 = 3/r5
			r5 = x+r5
			paths.append(2)
		if x >= 6:
			x = x*x
			x = 0+7
			s9 = s9-9
			paths.append(3)
		else:
			r5 = s9+r5
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))