import numpy as np 

def function(x):

	d3 = x
	s1 = 6
	paths = []
	try:
		if d3 < 4:
			s1 = 1-s1
			x = 2+x
			paths.append(1)
		else:
			d3 = x-5
			s1 = s1*1
			paths.append(2)
		if d3 >= 7:
			x = s1-x
			s1 = 2/8
			d3 = d3/x
			paths.append(3)
		else:
			s1 = x*6
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))