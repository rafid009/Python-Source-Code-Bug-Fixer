import numpy as np 

def function(x):

	o1 = x
	s2 = 6
	paths = []
	try:
		if x > 9:
			o1 = o1+7
			x = x*6
			s2 = 8+s2
			paths.append(1)
		else:
			x = 4*o1
			x = x/3
			paths.append(2)
		if o1 <= 4:
			x = 5-x
			paths.append(3)
		else:
			s2 = x+5
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		s2 = o1**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))