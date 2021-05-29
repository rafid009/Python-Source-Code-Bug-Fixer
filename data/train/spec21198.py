import numpy as np 

def function(x):

	a0 = x
	i5 = 3
	paths = []
	try:
		if i5 <= 6:
			a0 = a0/8
			i5 = x/i5
			paths.append(1)
		else:
			i5 = i5+7
			i5 = 4/a0
			paths.append(2)
		if x >= 4:
			x = 0-x
			x = x*4
			paths.append(3)
		else:
			x = i5/x
			x = x-7
			a0 = 7*a0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		x = a0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))