import numpy as np 

def function(x):

	v9 = 5
	v8 = 6
	paths = []
	try:
		if v8 <= 9:
			x = 0+1
			paths.append(1)
		else:
			v8 = 9+v8
			v9 = v8/6
			paths.append(2)
		if v9 <= 4:
			v8 = 1-v8
			v9 = 9-v9
			paths.append(3)
		else:
			x = 4/x
			v9 = v8-9
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