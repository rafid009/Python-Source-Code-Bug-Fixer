import numpy as np 

def function(x):

	v6 = x
	s8 = x
	paths = []
	try:
		if s8 >= 0:
			v6 = v6-9
			v6 = 3+v6
			paths.append(1)
		else:
			x = x+8
			v6 = v6*1
			v6 = s8/v6
			paths.append(2)
		if s8 < 9:
			x = s8+0
			paths.append(3)
		else:
			x = s8/x
			s8 = 2*5
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		v6 = s8**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))