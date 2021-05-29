import numpy as np 

def function(x):

	o1 = x
	a8 = 1
	paths = []
	try:
		if a8 < 4:
			x = x*1
			a8 = 4-a8
			paths.append(1)
		else:
			o1 = 8+o1
			o1 = a8+x
			paths.append(2)
		if x > 5:
			a8 = 5/3
			a8 = 9+a8
			o1 = o1*2
			paths.append(3)
		else:
			a8 = a8*4
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))