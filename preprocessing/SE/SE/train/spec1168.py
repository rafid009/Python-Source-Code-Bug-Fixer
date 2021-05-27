import numpy as np 

def function(x):

	v0 = 9
	k5 = 9
	paths = []
	try:
		if v0 > 8:
			v0 = 7/6
			v0 = 6*v0
			paths.append(1)
		else:
			v0 = 6+x
			paths.append(2)
		if x <= 2:
			x = 0/x
			v0 = 5-k5
			paths.append(3)
		else:
			k5 = 7-k5
			v0 = v0/4
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))