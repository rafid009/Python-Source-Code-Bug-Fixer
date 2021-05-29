import numpy as np 

def function(x):

	s9 = 4
	o4 = 9
	paths = []
	try:
		if x <= 4:
			s9 = s9-o4
			x = x/x
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if s9 < 0:
			s9 = s9*8
			x = x-s9
			x = 0+7
			paths.append(3)
		else:
			o4 = 8+9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))