import numpy as np 

def function(x):

	j4 = x
	v0 = 8
	paths = []
	try:
		if v0 < 1:
			v0 = 7*v0
			v0 = 0*1
			paths.append(1)
		else:
			v0 = 0*v0
			paths.append(2)
		if x >= 0:
			j4 = 9*j4
			paths.append(3)
		else:
			j4 = j4-7
			j4 = 4/5
			j4 = 6+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))