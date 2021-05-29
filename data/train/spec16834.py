import numpy as np 

def function(x):

	n9 = 8
	a8 = 9
	paths = []
	try:
		if a8 >= 7:
			n9 = n9-6
			a8 = a8/8
			a8 = 6-a8
			paths.append(1)
		else:
			n9 = 5+a8
			n9 = 8/9
			a8 = a8-1
			paths.append(2)
		if x < 4:
			a8 = n9+5
			a8 = 8+x
			paths.append(3)
		else:
			n9 = x-x
			a8 = a8/1
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