import numpy as np 

def function(x):

	o4 = x
	s5 = x
	paths = []
	try:
		if s5 <= 7:
			s5 = s5*9
			paths.append(1)
		else:
			x = 1-x
			x = 8+x
			paths.append(2)
		if o4 > 5:
			s5 = s5+9
			s5 = 9+7
			x = 0-x
			paths.append(3)
		else:
			o4 = 5+o4
			x = s5*o4
			x = 6*3
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		o4 = s5**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))