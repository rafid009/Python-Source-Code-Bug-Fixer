import numpy as np 

def function(x):

	o1 = x
	a8 = 5
	paths = []
	try:
		if o1 < 5:
			x = 3*6
			x = x+5
			paths.append(1)
		else:
			o1 = 4+9
			o1 = o1-9
			paths.append(2)
		if x >= 9:
			x = x+o1
			paths.append(3)
		else:
			a8 = a8*0
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))