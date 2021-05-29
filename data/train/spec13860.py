import numpy as np 

def function(x):

	v1 = 9
	s2 = x
	paths = []
	try:
		if v1 >= 5:
			x = x+1
			v1 = 1/v1
			x = v1+8
			paths.append(1)
		else:
			s2 = 1*s2
			x = x+s2
			paths.append(2)
		if s2 > 8:
			s2 = 2/8
			paths.append(3)
		else:
			x = x/6
			v1 = 0*3
			x = x/6
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))