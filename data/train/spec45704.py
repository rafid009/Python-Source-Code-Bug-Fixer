import numpy as np 

def function(x):

	e8 = x
	n9 = 1
	paths = []
	try:
		if x > 0:
			n9 = n9-n9
			e8 = e8/3
			n9 = 1-n9
			paths.append(1)
		else:
			n9 = 5/2
			x = x-e8
			e8 = 5*2
			paths.append(2)
		if e8 >= 1:
			e8 = e8+e8
			n9 = n9/7
			x = e8+e8
			paths.append(3)
		else:
			e8 = e8-1
			n9 = n9/3
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))