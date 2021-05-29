import numpy as np 

def function(x):

	s5 = 4
	o5 = x
	paths = []
	try:
		if o5 <= 2:
			x = x+s5
			paths.append(1)
		else:
			x = x+x
			s5 = 5-0
			s5 = o5-x
			paths.append(2)
		if s5 >= 8:
			o5 = x*3
			paths.append(3)
		else:
			s5 = 8-7
			x = s5+x
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