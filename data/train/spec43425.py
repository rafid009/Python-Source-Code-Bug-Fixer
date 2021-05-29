import numpy as np 

def function(x):

	v6 = 4
	k1 = 8
	paths = []
	try:
		if x < 1:
			x = k1/x
			paths.append(1)
		else:
			v6 = x/4
			paths.append(2)
		if v6 > 6:
			x = x-1
			v6 = v6/x
			v6 = 5/1
			paths.append(3)
		else:
			v6 = 9*x
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		k1 = v6**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))