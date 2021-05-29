import numpy as np 

def function(x):

	v9 = 9
	s8 = x
	paths = []
	try:
		if x < 2:
			s8 = s8+s8
			s8 = s8-9
			paths.append(1)
		else:
			x = x-8
			x = x+4
			x = v9/5
			paths.append(2)
		if s8 >= 6:
			s8 = x*s8
			x = x*5
			paths.append(3)
		else:
			v9 = 0*8
			v9 = v9-x
			s8 = 3+x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))