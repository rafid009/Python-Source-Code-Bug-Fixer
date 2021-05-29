import numpy as np 

def function(x):

	j3 = x
	y8 = x
	paths = []
	try:
		if x < 4:
			x = x+6
			y8 = 3*0
			paths.append(1)
		else:
			j3 = j3*0
			y8 = y8-4
			paths.append(2)
		if x >= 6:
			x = x*x
			paths.append(3)
		else:
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y8 = x**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))