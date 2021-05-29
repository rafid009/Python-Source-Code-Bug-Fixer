import numpy as np 

def function(x):

	s4 = x
	b0 = 3
	paths = []
	try:
		if x > 6:
			b0 = b0+b0
			s4 = s4+b0
			s4 = 6*4
			paths.append(1)
		else:
			b0 = 4+x
			x = x*s4
			x = s4+x
			paths.append(2)
		if x > 3:
			x = x*b0
			paths.append(3)
		else:
			b0 = b0+9
			b0 = b0+s4
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))