import numpy as np 

def function(x):

	s0 = 1
	j7 = x
	paths = []
	try:
		if j7 >= 7:
			s0 = s0+s0
			x = x/1
			paths.append(1)
		else:
			j7 = j7*4
			paths.append(2)
		if j7 < 0:
			x = 3/x
			j7 = j7*6
			paths.append(3)
		else:
			j7 = j7+8
			x = x-0
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))