import numpy as np 

def function(x):

	f8 = 9
	s2 = x
	paths = []
	try:
		if f8 < 5:
			s2 = s2/3
			paths.append(1)
		else:
			x = 8/2
			x = 4+x
			paths.append(2)
		if s2 >= 7:
			x = x*2
			s2 = s2-f8
			paths.append(3)
		else:
			x = 4-1
			f8 = 5*f8
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