import numpy as np 

def function(x):

	v1 = x
	k5 = 5
	paths = []
	try:
		if x < 6:
			x = 4/x
			x = 2/x
			paths.append(1)
		else:
			k5 = k5-4
			v1 = v1-v1
			k5 = k5*k5
			paths.append(2)
		if k5 > 7:
			k5 = k5*k5
			v1 = 8/3
			paths.append(3)
		else:
			k5 = 2*9
			x = x*3
			k5 = k5-8
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		k5 = v1**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))