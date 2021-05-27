import numpy as np 

def function(x):

	s2 = 5
	v5 = x
	paths = []
	try:
		if s2 >= 7:
			s2 = s2-5
			paths.append(1)
		else:
			x = 0*v5
			v5 = v5*6
			paths.append(2)
		if v5 < 9:
			v5 = 7*v5
			s2 = s2+8
			x = x-1
			paths.append(3)
		else:
			v5 = v5+6
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))