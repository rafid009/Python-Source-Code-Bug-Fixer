import numpy as np 

def function(x):

	a1 = 7
	n5 = x
	x = x
	paths = []
	try:
		if a1 > 3:
			n5 = 9-x
			a1 = 5-a1
			paths.append(1)
		else:
			a1 = a1*4
			n5 = n5-4
			a1 = 0-a1
			paths.append(2)
		if a1 > 9:
			x = x-a1
			a1 = a1/5
			x = n5-x
			paths.append(3)
		else:
			n5 = a1-7
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))