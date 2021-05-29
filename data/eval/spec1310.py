import numpy as np 

def function(x):

	a8 = x
	v1 = x
	paths = []
	try:
		if x >= 4:
			v1 = v1/x
			a8 = 2+a8
			paths.append(1)
		else:
			a8 = 2/a8
			x = 2*a8
			paths.append(2)
		if v1 < 6:
			x = 3/a8
			paths.append(3)
		else:
			v1 = v1*6
			x = x+9
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