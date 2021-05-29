import numpy as np 

def function(x):

	a8 = x
	j6 = 9
	paths = []
	try:
		if x < 8:
			j6 = 6*j6
			x = x-j6
			x = a8-x
			paths.append(1)
		else:
			j6 = 2+6
			j6 = 9+j6
			j6 = 5/9
			paths.append(2)
		if j6 < 3:
			a8 = 8+a8
			a8 = 8-a8
			a8 = a8/8
			paths.append(3)
		else:
			a8 = j6*j6
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))