import numpy as np 

def function(x):

	v6 = 8
	v2 = x
	paths = []
	try:
		if v6 >= 5:
			x = x*4
			paths.append(1)
		else:
			x = 5-1
			paths.append(2)
		if v6 >= 4:
			x = x+7
			paths.append(3)
		else:
			v2 = 1/v2
			v2 = 3-v2
			v6 = 5-2
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))