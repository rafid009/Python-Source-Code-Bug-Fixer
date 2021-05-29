import numpy as np 

def function(x):

	n7 = 1
	o9 = x
	paths = []
	try:
		if n7 > 9:
			o9 = n7/6
			x = 4-8
			paths.append(1)
		else:
			n7 = n7-6
			x = 4-x
			paths.append(2)
		if x < 1:
			x = 5+x
			paths.append(3)
		else:
			x = x/n7
			n7 = 5*n7
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		n7 = o9**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))