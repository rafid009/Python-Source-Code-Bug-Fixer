import numpy as np 

def function(x):

	v5 = x
	s6 = x
	paths = []
	try:
		if v5 > 6:
			s6 = s6*6
			x = x*x
			paths.append(1)
		else:
			s6 = s6*5
			x = 4+0
			paths.append(2)
		if s6 > 2:
			v5 = 0-v5
			s6 = v5+0
			v5 = 6-v5
			paths.append(3)
		else:
			v5 = 3+7
			s6 = 2*s6
			v5 = v5+x
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x = s6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))