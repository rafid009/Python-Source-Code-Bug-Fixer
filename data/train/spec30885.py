import numpy as np 

def function(x):

	o2 = 1
	s2 = x
	x = x
	paths = []
	try:
		if o2 > 4:
			o2 = s2/1
			s2 = x*s2
			o2 = x/2
			paths.append(1)
		else:
			x = x/o2
			x = x-7
			o2 = o2-4
			paths.append(2)
		if x <= 9:
			s2 = 9+x
			paths.append(3)
		else:
			x = 6-o2
			s2 = s2+6
			o2 = s2/o2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))