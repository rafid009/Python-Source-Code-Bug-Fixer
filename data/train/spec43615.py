import numpy as np 

def function(x):

	v8 = x
	s7 = 9
	paths = []
	try:
		if s7 > 5:
			x = x+9
			v8 = v8/1
			paths.append(1)
		else:
			v8 = 4*v8
			paths.append(2)
		if s7 < 3:
			v8 = 8/v8
			s7 = s7-3
			v8 = 8-s7
			paths.append(3)
		else:
			v8 = 3-x
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))