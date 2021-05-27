import numpy as np 

def function(x):

	s7 = 8
	o2 = x
	paths = []
	try:
		if o2 > 1:
			s7 = s7*9
			paths.append(1)
		else:
			s7 = x-s7
			s7 = s7*0
			x = 7/o2
			paths.append(2)
		if s7 <= 1:
			x = 2-x
			x = s7+x
			paths.append(3)
		else:
			o2 = o2-o2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))