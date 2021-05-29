import numpy as np 

def function(x):

	v8 = x
	s8 = x
	paths = []
	try:
		if v8 < 3:
			x = 6*x
			paths.append(1)
		else:
			s8 = x-v8
			paths.append(2)
		if x > 0:
			x = x/2
			paths.append(3)
		else:
			x = s8/5
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))