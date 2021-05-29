import numpy as np 

def function(x):

	o9 = x
	a1 = 3
	paths = []
	try:
		if a1 >= 2:
			x = x+x
			x = 9/x
			o9 = o9/2
			paths.append(1)
		else:
			o9 = o9+6
			paths.append(2)
		if a1 < 1:
			o9 = 4/o9
			o9 = o9-a1
			x = 8-x
			paths.append(3)
		else:
			a1 = x+a1
			o9 = a1*o9
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		a1 = o9**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))