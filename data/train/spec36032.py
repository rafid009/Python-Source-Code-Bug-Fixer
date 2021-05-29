import numpy as np 

def function(x):

	s4 = 3
	o9 = 6
	paths = []
	try:
		if x > 8:
			x = 4-x
			paths.append(1)
		else:
			s4 = 6/s4
			o9 = 6+x
			paths.append(2)
		if o9 <= 8:
			x = x*9
			paths.append(3)
		else:
			x = s4/6
			o9 = o9-s4
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		s4 = o9**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))