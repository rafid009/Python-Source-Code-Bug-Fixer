import numpy as np 

def function(x):

	o9 = 6
	s5 = 8
	paths = []
	try:
		if s5 >= 2:
			x = x-x
			o9 = 8/o9
			paths.append(1)
		else:
			x = x+3
			x = x*9
			paths.append(2)
		if s5 <= 4:
			o9 = o9*s5
			paths.append(3)
		else:
			s5 = o9-s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x = s5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))