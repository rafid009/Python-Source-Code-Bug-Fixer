import numpy as np 

def function(x):

	j3 = x
	y4 = 6
	paths = []
	try:
		if x >= 2:
			j3 = 9*4
			j3 = 9*2
			paths.append(1)
		else:
			j3 = j3+7
			y4 = 4+y4
			x = x+7
			paths.append(2)
		if y4 < 0:
			x = 5-x
			paths.append(3)
		else:
			y4 = j3+y4
			x = x/2
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