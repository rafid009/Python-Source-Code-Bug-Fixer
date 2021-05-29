import numpy as np 

def function(x):

	s5 = x
	v4 = x
	paths = []
	try:
		if s5 < 1:
			v4 = v4+1
			paths.append(1)
		else:
			s5 = v4/4
			paths.append(2)
		if s5 > 4:
			v4 = 2+s5
			s5 = s5*7
			s5 = v4/3
			paths.append(3)
		else:
			v4 = 7*v4
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