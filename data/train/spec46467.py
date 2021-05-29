import numpy as np 

def function(x):

	j3 = 7
	x4 = x
	paths = []
	try:
		if x4 < 8:
			x = x-7
			x = x-0
			paths.append(1)
		else:
			j3 = x4-j3
			x4 = x4-7
			paths.append(2)
		if x4 > 9:
			x = x*6
			paths.append(3)
		else:
			j3 = j3*4
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