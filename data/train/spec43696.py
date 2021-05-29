import numpy as np 

def function(x):

	o5 = 8
	s1 = 0
	paths = []
	try:
		if s1 < 9:
			s1 = s1/5
			s1 = 8*4
			paths.append(1)
		else:
			o5 = 0+1
			s1 = x-x
			o5 = o5+8
			paths.append(2)
		if s1 <= 9:
			o5 = o5-8
			x = o5+2
			s1 = x/s1
			paths.append(3)
		else:
			x = 8-x
			s1 = o5*0
			s1 = 8-s1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))