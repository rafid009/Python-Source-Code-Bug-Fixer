import numpy as np 

def function(x):

	j1 = x
	v8 = x
	paths = []
	try:
		if x <= 0:
			j1 = j1/5
			v8 = v8-v8
			j1 = 1-j1
			paths.append(1)
		else:
			x = 0/6
			paths.append(2)
		if j1 < 6:
			v8 = 0-v8
			paths.append(3)
		else:
			x = j1-4
			x = v8+7
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))