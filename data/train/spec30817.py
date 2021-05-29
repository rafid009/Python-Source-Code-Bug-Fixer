import numpy as np 

def function(x):

	o4 = x
	a0 = 4
	x = x
	paths = []
	try:
		if a0 < 8:
			a0 = 7/a0
			a0 = a0/1
			a0 = x+o4
			paths.append(1)
		else:
			a0 = a0-a0
			x = 7+x
			a0 = a0-5
			paths.append(2)
		if x > 4:
			a0 = a0+3
			x = 1/x
			x = 6*7
			paths.append(3)
		else:
			o4 = 2+o4
			a0 = a0-0
			o4 = x+0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))