import numpy as np 

def function(x):

	l3 = x
	o9 = 3
	paths = []
	try:
		if x > 4:
			x = x*0
			l3 = 7*l3
			paths.append(1)
		else:
			l3 = 4+o9
			paths.append(2)
		if l3 > 3:
			x = x+6
			paths.append(3)
		else:
			x = 3/o9
			l3 = 7-x
			o9 = o9+l3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))