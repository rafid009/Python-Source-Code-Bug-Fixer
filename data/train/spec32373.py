import numpy as np 

def function(x):

	j6 = x
	x7 = 2
	paths = []
	try:
		if x7 > 7:
			x = x/1
			x = 2+x
			paths.append(1)
		else:
			x = x/x
			x7 = x7/j6
			x7 = 0+j6
			paths.append(2)
		if j6 < 7:
			x7 = x7/9
			x7 = x7/x
			paths.append(3)
		else:
			j6 = 9+j6
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		j6 = x7**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))