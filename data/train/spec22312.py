import numpy as np 

def function(x):

	s6 = x
	v8 = x
	paths = []
	try:
		if s6 < 3:
			v8 = v8-6
			paths.append(1)
		else:
			x = 2-v8
			v8 = v8-6
			paths.append(2)
		if x < 1:
			v8 = 7-v8
			paths.append(3)
		else:
			x = x+x
			v8 = s6-v8
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