import numpy as np 

def function(x):

	j3 = 3
	s9 = 7
	paths = []
	try:
		if x <= 6:
			j3 = 2*s9
			j3 = j3/4
			paths.append(1)
		else:
			s9 = j3/3
			paths.append(2)
		if x < 8:
			j3 = j3+5
			paths.append(3)
		else:
			x = 7/7
			j3 = j3-s9
			s9 = j3*3
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