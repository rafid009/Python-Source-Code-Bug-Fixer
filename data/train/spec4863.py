import numpy as np 

def function(x):

	j3 = x
	s4 = x
	paths = []
	try:
		if s4 >= 2:
			x = j3*1
			paths.append(1)
		else:
			j3 = j3+x
			j3 = j3/2
			paths.append(2)
		if s4 <= 5:
			j3 = 5*j3
			x = 7/s4
			paths.append(3)
		else:
			x = s4/s4
			j3 = 3*s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))