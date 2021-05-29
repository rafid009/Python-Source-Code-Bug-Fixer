import numpy as np 

def function(x):

	s0 = x
	o6 = x
	paths = []
	try:
		if o6 > 1:
			s0 = s0+x
			x = x+o6
			o6 = s0-o6
			paths.append(1)
		else:
			s0 = 8+s0
			o6 = 7*0
			o6 = o6-5
			paths.append(2)
		if x > 3:
			s0 = x*s0
			paths.append(3)
		else:
			s0 = s0*6
			o6 = 3+o6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))