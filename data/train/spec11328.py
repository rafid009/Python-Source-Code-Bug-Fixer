import numpy as np 

def function(x):

	o9 = x
	n7 = x
	paths = []
	try:
		if n7 <= 5:
			n7 = 6/7
			paths.append(1)
		else:
			x = 9/x
			n7 = n7-x
			n7 = n7*o9
			paths.append(2)
		if x < 9:
			x = x/x
			paths.append(3)
		else:
			n7 = 2/2
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))