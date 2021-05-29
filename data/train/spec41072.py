import numpy as np 

def function(x):

	o5 = 7
	s1 = x
	paths = []
	try:
		if x < 5:
			x = 6*x
			o5 = o5*4
			paths.append(1)
		else:
			s1 = 7+s1
			paths.append(2)
		if o5 <= 7:
			o5 = x-8
			x = 7+o5
			paths.append(3)
		else:
			o5 = 6-6
			s1 = 2*s1
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		o5 = o5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))