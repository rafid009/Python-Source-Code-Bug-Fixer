import numpy as np 

def function(x):

	d2 = x
	j9 = x
	paths = []
	try:
		if d2 < 4:
			j9 = 0+j9
			paths.append(1)
		else:
			j9 = 2/9
			j9 = d2*7
			x = x-x
			paths.append(2)
		if x <= 0:
			d2 = d2*7
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))