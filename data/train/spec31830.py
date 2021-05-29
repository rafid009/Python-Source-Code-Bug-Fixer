import numpy as np 

def function(x):

	i6 = 5
	s4 = 4
	paths = []
	try:
		if s4 <= 5:
			x = x-5
			paths.append(1)
		else:
			x = x+i6
			paths.append(2)
		if i6 >= 4:
			s4 = s4*3
			s4 = s4+s4
			s4 = 9-x
			paths.append(3)
		else:
			i6 = i6-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))