import numpy as np 

def function(x):

	o0 = x
	s4 = x
	paths = []
	try:
		if o0 < 1:
			o0 = o0+2
			paths.append(1)
		else:
			o0 = o0-7
			o0 = o0-7
			o0 = 1+9
			paths.append(2)
		if s4 <= 6:
			o0 = o0/1
			s4 = s4*1
			o0 = o0+x
			paths.append(3)
		else:
			o0 = s4/6
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		s4 = o0**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))