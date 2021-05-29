import numpy as np 

def function(x):

	y1 = 0
	j3 = x
	paths = []
	try:
		if y1 > 8:
			y1 = y1/7
			x = x-j3
			paths.append(1)
		else:
			j3 = j3-0
			j3 = 6-4
			paths.append(2)
		if x > 5:
			j3 = j3-j3
			j3 = 0+2
			paths.append(3)
		else:
			x = x-6
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