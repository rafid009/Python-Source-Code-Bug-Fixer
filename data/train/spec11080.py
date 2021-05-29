import numpy as np 

def function(x):

	s4 = x
	v9 = x
	paths = []
	try:
		if s4 >= 4:
			x = x*x
			s4 = v9+s4
			paths.append(1)
		else:
			s4 = s4-0
			paths.append(2)
		if x >= 7:
			v9 = s4+8
			s4 = s4/1
			x = x-9
			paths.append(3)
		else:
			v9 = 7/v9
			x = x+9
			x = 5*6
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))