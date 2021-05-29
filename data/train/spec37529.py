import numpy as np 

def function(x):

	i2 = 9
	s4 = x
	paths = []
	try:
		if x <= 6:
			x = 2+x
			s4 = 4-x
			paths.append(1)
		else:
			i2 = i2*9
			paths.append(2)
		if x < 4:
			s4 = 7+i2
			i2 = i2-x
			paths.append(3)
		else:
			x = s4-2
			s4 = s4/s4
			x = s4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))