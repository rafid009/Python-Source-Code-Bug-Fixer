import numpy as np 

def function(x):

	o0 = x
	s7 = x
	x = x
	paths = []
	try:
		if x <= 5:
			x = 5-x
			paths.append(1)
		else:
			o0 = 5-o0
			paths.append(2)
		if s7 < 4:
			x = 0*x
			paths.append(3)
		else:
			o0 = o0/1
			x = o0-8
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))