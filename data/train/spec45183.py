import numpy as np 

def function(x):

	v4 = 9
	s1 = 7
	paths = []
	try:
		if s1 < 7:
			x = v4/4
			paths.append(1)
		else:
			v4 = v4*s1
			x = x*0
			v4 = 3-v4
			paths.append(2)
		if x > 2:
			x = v4-x
			v4 = 1/1
			v4 = v4*2
			paths.append(3)
		else:
			v4 = 9+v4
			s1 = 1-s1
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))