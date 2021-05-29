import numpy as np 

def function(x):

	i0 = x
	s2 = 0
	paths = []
	try:
		if x < 6:
			i0 = 8-0
			paths.append(1)
		else:
			s2 = s2+s2
			i0 = x+s2
			paths.append(2)
		if i0 > 1:
			i0 = 0-i0
			paths.append(3)
		else:
			i0 = 9/1
			x = x-5
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))