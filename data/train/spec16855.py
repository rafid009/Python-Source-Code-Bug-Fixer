import numpy as np 

def function(x):

	a8 = x
	k5 = 9
	paths = []
	try:
		if k5 > 9:
			x = x*k5
			x = x+x
			a8 = x/a8
			paths.append(1)
		else:
			x = k5+x
			a8 = 9*k5
			paths.append(2)
		if x <= 7:
			k5 = 5+x
			k5 = 1/1
			paths.append(3)
		else:
			a8 = 0-k5
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		k5 = a8**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))