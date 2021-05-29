import numpy as np 

def function(x):

	i8 = 7
	k5 = 1
	x = x
	paths = []
	try:
		if x <= 5:
			k5 = k5/4
			paths.append(1)
		else:
			x = x+9
			x = x/1
			paths.append(2)
		if k5 > 2:
			k5 = 1/k5
			paths.append(3)
		else:
			k5 = k5*0
			i8 = 2/2
			x = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i8 = x**0.5
		return i8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))