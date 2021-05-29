import numpy as np 

def function(x):

	i8 = 9
	s6 = x
	paths = []
	try:
		if i8 <= 8:
			i8 = 8+8
			paths.append(1)
		else:
			i8 = i8*9
			s6 = s6-2
			x = 1*s6
			paths.append(2)
		if x > 2:
			i8 = i8*4
			x = x+x
			i8 = 3*4
			paths.append(3)
		else:
			i8 = i8*s6
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