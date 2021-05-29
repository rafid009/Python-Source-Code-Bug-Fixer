import numpy as np 

def function(x):

	v1 = x
	f1 = 1
	paths = []
	try:
		if x > 4:
			x = x/7
			x = v1/f1
			v1 = 1/v1
			paths.append(1)
		else:
			v1 = v1+7
			v1 = v1+f1
			paths.append(2)
		if f1 <= 6:
			v1 = v1+f1
			paths.append(3)
		else:
			v1 = 4+8
			x = f1*9
			f1 = f1+f1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))