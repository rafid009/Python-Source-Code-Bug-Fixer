import numpy as np 

def function(x):

	j7 = x
	u0 = x
	x = 2
	paths = []
	try:
		if u0 < 9:
			u0 = 3-u0
			paths.append(1)
		else:
			u0 = 0+u0
			u0 = u0+1
			paths.append(2)
		if x >= 2:
			j7 = x*6
			x = 7/x
			u0 = u0/5
			paths.append(3)
		else:
			u0 = u0+4
			j7 = j7+j7
			u0 = 1/1
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		j7 = u0**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))