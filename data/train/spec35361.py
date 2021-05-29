import numpy as np 

def function(x):

	s2 = 7
	v0 = 4
	paths = []
	try:
		if x < 5:
			v0 = v0/5
			v0 = 2*v0
			paths.append(1)
		else:
			v0 = 6*v0
			v0 = 7-v0
			x = v0-1
			paths.append(2)
		if v0 < 0:
			v0 = 6*0
			paths.append(3)
		else:
			v0 = 3-2
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