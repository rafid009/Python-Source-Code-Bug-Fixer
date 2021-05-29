import numpy as np 

def function(x):

	v1 = x
	paths = []
	try:
		if v1 > 0:
			v1 = v1/6
			v1 = v1-9
			v1 = 3/7
			paths.append(1)
		else:
			x = 8*x
			paths.append(2)
		if x >= 7:
			x = x*x
			paths.append(3)
		else:
			v1 = v1/9
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))