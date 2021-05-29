import numpy as np 

def function(x):

	v6 = 6
	q8 = x
	paths = []
	try:
		if x >= 9:
			q8 = q8-5
			q8 = 8*3
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if x > 4:
			v6 = v6-x
			paths.append(3)
		else:
			v6 = v6*5
			q8 = q8*x
			x = 3-9
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		x = v6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))