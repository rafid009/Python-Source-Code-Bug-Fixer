import numpy as np 

def function(x):

	a8 = 2
	k7 = x
	paths = []
	try:
		if x < 4:
			a8 = x/a8
			x = x-8
			k7 = 5+a8
			paths.append(1)
		else:
			k7 = x/x
			x = x*5
			x = 8-2
			paths.append(2)
		if x > 0:
			x = 6-x
			x = x-2
			paths.append(3)
		else:
			a8 = 2*k7
			a8 = 6+a8
			a8 = k7-6
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