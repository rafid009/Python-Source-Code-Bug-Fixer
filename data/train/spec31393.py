import numpy as np 

def function(x):

	x3 = x
	v9 = 3
	paths = []
	try:
		if v9 < 9:
			x = 6*x
			paths.append(1)
		else:
			x = 5+v9
			paths.append(2)
		if x >= 8:
			v9 = v9/7
			x = x-8
			x = 5-x
			paths.append(3)
		else:
			v9 = x3+x3
			v9 = v9*2
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x3 = v9**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))