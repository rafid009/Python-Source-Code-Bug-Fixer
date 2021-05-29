import numpy as np 

def function(x):

	o2 = x
	s7 = x
	x = x
	paths = []
	try:
		if s7 <= 0:
			o2 = 8*o2
			s7 = 2+s7
			paths.append(1)
		else:
			x = s7+x
			s7 = s7+1
			o2 = o2*o2
			paths.append(2)
		if o2 > 1:
			s7 = 4-o2
			x = x/3
			o2 = o2+2
			paths.append(3)
		else:
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))