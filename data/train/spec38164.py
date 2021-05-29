import numpy as np 

def function(x):

	k7 = 3
	f1 = x
	paths = []
	try:
		if k7 >= 5:
			k7 = 9-9
			paths.append(1)
		else:
			k7 = x-2
			f1 = f1*5
			paths.append(2)
		if x > 3:
			k7 = k7+3
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))