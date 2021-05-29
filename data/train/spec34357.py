import numpy as np 

def function(x):

	o1 = 9
	s6 = 5
	paths = []
	try:
		if s6 > 4:
			o1 = 1-o1
			o1 = o1+o1
			s6 = s6-7
			paths.append(1)
		else:
			s6 = s6+x
			s6 = s6*0
			paths.append(2)
		if o1 < 8:
			x = 6-x
			paths.append(3)
		else:
			s6 = o1-o1
			o1 = o1-0
			x = x-5
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		s6 = o1**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))