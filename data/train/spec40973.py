import numpy as np 

def function(x):

	o1 = x
	a2 = 6
	paths = []
	try:
		if o1 >= 3:
			x = x+6
			a2 = a2/2
			o1 = 3/o1
			paths.append(1)
		else:
			o1 = x-a2
			o1 = 8+o1
			o1 = o1/6
			paths.append(2)
		if a2 <= 9:
			a2 = a2/1
			paths.append(3)
		else:
			x = 2-7
			x = a2+1
			x = x+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))