import numpy as np 

def function(x):

	e9 = 3
	i9 = x
	paths = []
	try:
		if e9 < 9:
			e9 = x/3
			paths.append(1)
		else:
			i9 = x/1
			paths.append(2)
		if x <= 8:
			x = 8/x
			e9 = x*2
			x = x/x
			paths.append(3)
		else:
			x = 1/9
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))