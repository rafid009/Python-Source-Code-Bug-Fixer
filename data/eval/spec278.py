import numpy as np 

def function(x):

	o6 = 7
	a9 = 4
	paths = []
	try:
		if x <= 9:
			a9 = 6-x
			o6 = 3+o6
			x = 8+0
			paths.append(1)
		else:
			a9 = 0*a9
			x = 4+9
			o6 = 5-o6
			paths.append(2)
		if o6 >= 4:
			x = a9*a9
			a9 = 5+o6
			paths.append(3)
		else:
			x = x+a9
			x = o6-a9
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))