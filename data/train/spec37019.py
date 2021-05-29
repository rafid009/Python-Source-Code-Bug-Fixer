import numpy as np 

def function(x):

	a8 = x
	o9 = 4
	paths = []
	try:
		if a8 > 9:
			x = 1/o9
			paths.append(1)
		else:
			a8 = 1+a8
			paths.append(2)
		if o9 > 4:
			o9 = o9+1
			o9 = x+4
			paths.append(3)
		else:
			o9 = o9*2
			x = 1/a8
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