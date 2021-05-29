import numpy as np 

def function(x):

	o8 = x
	s5 = 1
	paths = []
	try:
		if o8 > 0:
			s5 = 3+0
			paths.append(1)
		else:
			s5 = s5/4
			x = 1+x
			o8 = x+5
			paths.append(2)
		if x < 0:
			s5 = s5+6
			paths.append(3)
		else:
			o8 = 1+o8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		x = o8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))