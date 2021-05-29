import numpy as np 

def function(x):

	s6 = 4
	o3 = 8
	paths = []
	try:
		if x < 1:
			s6 = 6/s6
			o3 = 4/o3
			x = 1-o3
			paths.append(1)
		else:
			x = x/6
			s6 = s6+o3
			paths.append(2)
		if x > 9:
			o3 = 0-6
			paths.append(3)
		else:
			s6 = 8+s6
			x = x*9
			s6 = s6+x
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		o3 = o3**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))