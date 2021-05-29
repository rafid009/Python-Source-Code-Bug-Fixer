import numpy as np 

def function(x):

	a6 = x
	v5 = 2
	paths = []
	try:
		if x >= 9:
			x = x-a6
			x = x+0
			paths.append(1)
		else:
			a6 = a6/1
			paths.append(2)
		if v5 < 5:
			a6 = a6+6
			a6 = v5/a6
			v5 = 7+v5
			paths.append(3)
		else:
			a6 = 8/a6
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		a6 = a6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))