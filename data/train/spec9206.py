import numpy as np 

def function(x):

	o8 = x
	s5 = 0
	paths = []
	try:
		if s5 <= 0:
			x = 9/x
			s5 = s5+6
			s5 = 7-s5
			paths.append(1)
		else:
			s5 = 4+5
			s5 = 8/3
			o8 = 9+9
			paths.append(2)
		if o8 < 5:
			o8 = o8/s5
			x = x*x
			paths.append(3)
		else:
			x = 8-1
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))