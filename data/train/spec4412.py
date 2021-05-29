import numpy as np 

def function(x):

	s5 = x
	v8 = 2
	paths = []
	try:
		if v8 <= 5:
			s5 = 0*v8
			paths.append(1)
		else:
			s5 = 9+s5
			v8 = x+9
			x = 5+4
			paths.append(2)
		if s5 > 6:
			s5 = s5/7
			x = x+x
			paths.append(3)
		else:
			v8 = v8/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))