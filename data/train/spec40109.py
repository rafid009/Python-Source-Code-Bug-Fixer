import numpy as np 

def function(x):

	k1 = x
	f1 = x
	paths = []
	try:
		if f1 < 0:
			k1 = k1-0
			x = 5+3
			paths.append(1)
		else:
			f1 = 3+f1
			paths.append(2)
		if k1 < 9:
			x = 7/x
			x = x*f1
			x = f1-8
			paths.append(3)
		else:
			f1 = x-f1
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		k1 = f1**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))