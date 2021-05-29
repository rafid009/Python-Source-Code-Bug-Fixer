import numpy as np 

def function(x):

	k5 = x
	v8 = 7
	paths = []
	try:
		if k5 >= 7:
			x = 9/v8
			x = 2-0
			paths.append(1)
		else:
			k5 = 0/6
			paths.append(2)
		if x <= 5:
			k5 = 2+k5
			v8 = 6*v8
			paths.append(3)
		else:
			x = 9/5
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))