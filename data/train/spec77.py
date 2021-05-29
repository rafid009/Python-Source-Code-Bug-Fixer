import numpy as np 

def function(x):

	s6 = x
	j7 = 1
	paths = []
	try:
		if s6 > 4:
			j7 = j7*9
			x = 0+x
			x = j7+0
			paths.append(1)
		else:
			j7 = j7/j7
			paths.append(2)
		if j7 > 7:
			s6 = 8/7
			j7 = j7-x
			paths.append(3)
		else:
			j7 = j7/6
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