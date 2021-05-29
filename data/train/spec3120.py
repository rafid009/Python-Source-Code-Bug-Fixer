import numpy as np 

def function(x):

	o6 = x
	s5 = 4
	paths = []
	try:
		if o6 > 7:
			o6 = o6*6
			s5 = s5*8
			paths.append(1)
		else:
			s5 = x+s5
			x = o6+1
			s5 = 1/x
			paths.append(2)
		if s5 >= 8:
			o6 = 3*s5
			s5 = x*s5
			s5 = 3*s5
			paths.append(3)
		else:
			s5 = s5/5
			x = x-x
			s5 = s5+s5
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		s5 = o6**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))