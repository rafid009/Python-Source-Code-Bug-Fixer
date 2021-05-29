import numpy as np 

def function(x):

	j4 = x
	v8 = 2
	paths = []
	try:
		if x > 6:
			v8 = v8/9
			j4 = 4+v8
			v8 = 2-v8
			paths.append(1)
		else:
			v8 = 9*v8
			paths.append(2)
		if x >= 3:
			x = 4+7
			x = x+0
			paths.append(3)
		else:
			x = x-v8
			j4 = j4+5
			x = x+v8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))