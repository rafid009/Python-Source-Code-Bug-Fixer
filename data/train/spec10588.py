import numpy as np 

def function(x):

	s7 = 9
	v6 = 1
	paths = []
	try:
		if s7 >= 8:
			x = x+6
			v6 = x*v6
			paths.append(1)
		else:
			x = 8/3
			v6 = 7+v6
			paths.append(2)
		if s7 > 5:
			x = x-2
			s7 = s7-0
			x = x+0
			paths.append(3)
		else:
			x = 1/x
			v6 = 2+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))