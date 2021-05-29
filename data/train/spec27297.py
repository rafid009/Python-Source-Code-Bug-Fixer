import numpy as np 

def function(x):

	s9 = 5
	o3 = 2
	paths = []
	try:
		if o3 <= 5:
			o3 = s9/1
			o3 = o3+o3
			s9 = 1-s9
			paths.append(1)
		else:
			o3 = o3/6
			x = 2/2
			s9 = 6-s9
			paths.append(2)
		if x > 8:
			o3 = 3-8
			s9 = s9-5
			s9 = s9/3
			paths.append(3)
		else:
			s9 = x/o3
			o3 = o3+5
			o3 = o3/9
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		s9 = o3**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))