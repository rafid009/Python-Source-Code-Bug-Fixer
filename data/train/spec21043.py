import numpy as np 

def function(x):

	s8 = 7
	v1 = x
	paths = []
	try:
		if x <= 1:
			x = 1*v1
			x = 9+x
			x = 6*2
			paths.append(1)
		else:
			v1 = 1*v1
			x = 2-x
			s8 = s8-2
			paths.append(2)
		if s8 > 1:
			x = x*s8
			x = x+s8
			s8 = x*v1
			paths.append(3)
		else:
			x = s8-6
			x = x/6
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		x = s8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))