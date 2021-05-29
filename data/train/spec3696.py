import numpy as np 

def function(x):

	d5 = 3
	s9 = x
	paths = []
	try:
		if x > 9:
			s9 = 9-4
			d5 = x/2
			x = s9+d5
			paths.append(1)
		else:
			d5 = 7-d5
			paths.append(2)
		if s9 > 7:
			d5 = d5+7
			s9 = 7*x
			d5 = d5-s9
			paths.append(3)
		else:
			x = d5+2
			x = 8-0
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))