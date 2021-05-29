import numpy as np 

def function(x):

	r4 = 7
	j3 = 7
	paths = []
	try:
		if j3 >= 7:
			j3 = x-j3
			paths.append(1)
		else:
			r4 = r4/r4
			paths.append(2)
		if j3 >= 2:
			j3 = j3/j3
			x = 9*j3
			j3 = 9*3
			paths.append(3)
		else:
			x = r4/8
			r4 = 4/6
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))