import numpy as np 

def function(x):

	s9 = x
	o9 = x
	paths = []
	try:
		if o9 >= 6:
			o9 = o9*3
			o9 = s9-7
			o9 = o9+6
			paths.append(1)
		else:
			s9 = s9+0
			o9 = o9+7
			o9 = 2-7
			paths.append(2)
		if s9 < 6:
			s9 = 3+s9
			o9 = x+7
			paths.append(3)
		else:
			s9 = o9*3
			o9 = 5*o9
			s9 = 3+s9
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