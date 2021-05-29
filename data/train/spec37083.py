import numpy as np 

def function(x):

	v5 = 4
	s7 = 6
	paths = []
	try:
		if v5 <= 6:
			x = x-6
			paths.append(1)
		else:
			s7 = 2*s7
			v5 = v5/8
			s7 = x/s7
			paths.append(2)
		if v5 > 7:
			x = 4/x
			v5 = 4*1
			v5 = x-v5
			paths.append(3)
		else:
			s7 = 5-s7
			v5 = v5*7
			v5 = 2+v5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))