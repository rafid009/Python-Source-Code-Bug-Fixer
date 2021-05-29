import numpy as np 

def function(x):

	s4 = 7
	r6 = x
	paths = []
	try:
		if x <= 4:
			s4 = r6+0
			paths.append(1)
		else:
			x = x-5
			r6 = 8+r6
			r6 = s4-r6
			paths.append(2)
		if s4 < 5:
			x = x/6
			r6 = r6-8
			paths.append(3)
		else:
			s4 = x+s4
			r6 = r6-x
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s4 = x**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))