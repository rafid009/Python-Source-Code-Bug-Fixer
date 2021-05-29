import numpy as np 

def function(x):

	x4 = x
	j3 = 9
	paths = []
	try:
		if x >= 6:
			x = x-3
			x = x-j3
			paths.append(1)
		else:
			j3 = 8/9
			x = j3+x4
			x = 5/x
			paths.append(2)
		if x4 > 4:
			x4 = 5+5
			paths.append(3)
		else:
			x4 = x4-x4
			j3 = 0+j3
			x4 = x*x
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