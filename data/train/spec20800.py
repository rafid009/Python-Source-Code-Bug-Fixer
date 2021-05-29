import numpy as np 

def function(x):

	s5 = 6
	r5 = x
	paths = []
	try:
		if x <= 7:
			s5 = 8+x
			paths.append(1)
		else:
			s5 = s5/3
			r5 = 6*r5
			r5 = 3*r5
			paths.append(2)
		if s5 >= 9:
			s5 = 2/s5
			s5 = 6-s5
			r5 = r5*3
			paths.append(3)
		else:
			r5 = 8*9
			x = 5+r5
			s5 = s5-2
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))