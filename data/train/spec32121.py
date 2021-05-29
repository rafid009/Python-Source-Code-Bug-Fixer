import numpy as np 

def function(x):

	k4 = 1
	v2 = x
	paths = []
	try:
		if k4 >= 5:
			x = x+v2
			k4 = 4-1
			paths.append(1)
		else:
			v2 = 7-k4
			paths.append(2)
		if v2 > 3:
			k4 = x+k4
			v2 = x-v2
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		k4 = v2**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))