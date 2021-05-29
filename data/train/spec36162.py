import numpy as np 

def function(x):

	v7 = x
	a1 = x
	paths = []
	try:
		if a1 < 5:
			x = 2+x
			paths.append(1)
		else:
			x = x*3
			v7 = 8+v7
			a1 = v7-a1
			paths.append(2)
		if v7 < 2:
			a1 = 3/a1
			paths.append(3)
		else:
			v7 = x/4
			v7 = 5+v7
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		a1 = v7**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))