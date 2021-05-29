import numpy as np 

def function(x):

	j7 = x
	s7 = 7
	paths = []
	try:
		if j7 < 6:
			x = s7+x
			paths.append(1)
		else:
			x = x/6
			x = x-x
			paths.append(2)
		if x > 7:
			s7 = 5+s7
			paths.append(3)
		else:
			j7 = j7-j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))