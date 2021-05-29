import numpy as np 

def function(x):

	s4 = x
	j8 = 8
	paths = []
	try:
		if s4 > 8:
			s4 = 8+1
			paths.append(1)
		else:
			s4 = 5+s4
			paths.append(2)
		if s4 >= 5:
			x = 5-0
			paths.append(3)
		else:
			j8 = 2*j8
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		j8 = s4**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))