import numpy as np 

def function(x):

	j3 = x
	s7 = x
	paths = []
	try:
		if j3 <= 8:
			x = 7/x
			x = x+7
			paths.append(1)
		else:
			s7 = s7/4
			j3 = j3-3
			paths.append(2)
		if j3 <= 2:
			x = 5/5
			paths.append(3)
		else:
			j3 = 9-9
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))