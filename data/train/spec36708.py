import numpy as np 

def function(x):

	v2 = 0
	x9 = 6
	paths = []
	try:
		if v2 < 8:
			x9 = v2/1
			x9 = x9-7
			x = 8-4
			paths.append(1)
		else:
			x = x+7
			x9 = 1*x9
			paths.append(2)
		if v2 <= 4:
			x = v2*x9
			v2 = v2+6
			paths.append(3)
		else:
			v2 = v2/1
			v2 = 8-9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))