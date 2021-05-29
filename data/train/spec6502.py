import numpy as np 

def function(x):

	v8 = x
	s1 = x
	paths = []
	try:
		if x > 9:
			s1 = 0+s1
			paths.append(1)
		else:
			s1 = s1-7
			v8 = 1*5
			s1 = s1/7
			paths.append(2)
		if x > 0:
			v8 = s1/4
			paths.append(3)
		else:
			v8 = 1*v8
			v8 = 3-v8
			v8 = v8/4
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