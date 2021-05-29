import numpy as np 

def function(x):

	v0 = x
	s5 = 2
	paths = []
	try:
		if s5 <= 2:
			v0 = v0-4
			v0 = 5-v0
			s5 = 6-s5
			paths.append(1)
		else:
			v0 = s5+v0
			s5 = s5+s5
			s5 = s5/3
			paths.append(2)
		if x > 1:
			v0 = x*v0
			paths.append(3)
		else:
			v0 = 4*v0
			v0 = v0/s5
			s5 = s5-s5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))