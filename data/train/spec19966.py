import numpy as np 

def function(x):

	s7 = 1
	i4 = 5
	paths = []
	try:
		if x >= 4:
			i4 = x/x
			s7 = 3+s7
			x = s7-5
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if i4 < 6:
			i4 = 0*0
			x = i4+x
			paths.append(3)
		else:
			i4 = i4-4
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