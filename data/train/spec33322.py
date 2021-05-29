import numpy as np 

def function(x):

	v4 = 6
	s9 = 9
	paths = []
	try:
		if v4 >= 4:
			s9 = s9/2
			v4 = 0-x
			s9 = 4/s9
			paths.append(1)
		else:
			s9 = s9+1
			v4 = v4+v4
			v4 = v4+v4
			paths.append(2)
		if x >= 6:
			v4 = v4/4
			s9 = v4/3
			v4 = 4*9
			paths.append(3)
		else:
			x = x+2
			x = v4+0
			x = x/8
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