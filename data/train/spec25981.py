import numpy as np 

def function(x):

	l1 = 3
	o9 = 1
	paths = []
	try:
		if o9 < 2:
			o9 = 5-x
			o9 = 6-x
			l1 = 5-o9
			paths.append(1)
		else:
			x = x-1
			o9 = 0+o9
			paths.append(2)
		if l1 <= 1:
			o9 = 4*o9
			x = x+6
			paths.append(3)
		else:
			l1 = x*l1
			l1 = l1-o9
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))