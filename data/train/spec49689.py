import numpy as np 

def function(x):

	s8 = 7
	o6 = x
	paths = []
	try:
		if x <= 5:
			o6 = 1*o6
			s8 = 5/x
			o6 = o6/o6
			paths.append(1)
		else:
			o6 = o6*2
			o6 = o6/8
			paths.append(2)
		if s8 <= 0:
			o6 = o6-8
			s8 = s8+2
			s8 = s8+1
			paths.append(3)
		else:
			o6 = o6*7
			x = o6*7
			s8 = 1-0
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		s8 = o6**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))