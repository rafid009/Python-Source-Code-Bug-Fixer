import numpy as np 

def function(x):

	e3 = x
	v7 = x
	paths = []
	try:
		if x < 9:
			x = 9-x
			v7 = v7*e3
			paths.append(1)
		else:
			v7 = e3+0
			paths.append(2)
		if v7 <= 6:
			x = v7*9
			e3 = 7+9
			paths.append(3)
		else:
			e3 = e3-9
			x = 3+2
			v7 = 3+7
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))