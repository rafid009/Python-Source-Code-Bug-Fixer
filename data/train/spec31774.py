import numpy as np 

def function(x):

	b0 = 3
	s8 = x
	x = 2
	paths = []
	try:
		if s8 < 6:
			x = b0*x
			paths.append(1)
		else:
			x = x+5
			x = 3+x
			x = x/9
			paths.append(2)
		if s8 > 1:
			b0 = 2/9
			paths.append(3)
		else:
			b0 = x-0
			x = 2-6
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