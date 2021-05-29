import numpy as np 

def function(x):

	v9 = 3
	paths = []
	try:
		if v9 >= 9:
			v9 = 5+8
			v9 = x+4
			paths.append(1)
		else:
			v9 = 2+5
			v9 = v9/v9
			x = 0/x
			paths.append(2)
		if v9 > 6:
			x = x-v9
			v9 = 5-v9
			paths.append(3)
		else:
			v9 = x-v9
			x = x-6
			v9 = v9*2
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))