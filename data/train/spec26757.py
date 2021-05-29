import numpy as np 

def function(x):

	a1 = x
	o1 = x
	paths = []
	try:
		if a1 <= 2:
			x = o1/6
			paths.append(1)
		else:
			x = a1*o1
			a1 = 4/x
			paths.append(2)
		if o1 <= 1:
			x = o1*3
			o1 = o1-0
			paths.append(3)
		else:
			o1 = 7*o1
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		a1 = o1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))