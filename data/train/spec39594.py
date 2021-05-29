import numpy as np 

def function(x):

	r9 = 4
	s5 = 9
	paths = []
	try:
		if r9 <= 7:
			r9 = r9-5
			s5 = 9+9
			paths.append(1)
		else:
			r9 = 9/3
			x = 8/s5
			r9 = x*r9
			paths.append(2)
		if s5 <= 4:
			r9 = 3*r9
			paths.append(3)
		else:
			x = r9*x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))