import numpy as np 

def function(x):

	o0 = 4
	s7 = 8
	paths = []
	try:
		if s7 <= 9:
			s7 = s7-2
			paths.append(1)
		else:
			x = s7-3
			x = x/o0
			x = x/3
			paths.append(2)
		if x <= 2:
			s7 = s7-0
			s7 = s7+x
			paths.append(3)
		else:
			o0 = o0+x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		o0 = s7**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))