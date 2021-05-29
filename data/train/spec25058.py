import numpy as np 

def function(x):

	o2 = 2
	s9 = 7
	paths = []
	try:
		if s9 < 5:
			x = x/2
			o2 = x-o2
			paths.append(1)
		else:
			x = o2-4
			s9 = s9-6
			paths.append(2)
		if x < 1:
			s9 = s9*6
			o2 = 9-2
			paths.append(3)
		else:
			o2 = s9/5
			o2 = o2+7
			o2 = 1/o2
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