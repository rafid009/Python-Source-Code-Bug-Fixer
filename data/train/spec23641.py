import numpy as np 

def function(x):

	d1 = 1
	j3 = 6
	paths = []
	try:
		if j3 > 3:
			x = 0-x
			d1 = d1*j3
			paths.append(1)
		else:
			x = 6*2
			paths.append(2)
		if j3 < 1:
			x = 9-x
			j3 = j3/9
			paths.append(3)
		else:
			d1 = 0-d1
			j3 = 4/j3
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))