import numpy as np 

def function(x):

	v0 = x
	a1 = x
	paths = []
	try:
		if v0 > 3:
			a1 = a1*3
			paths.append(1)
		else:
			x = x-x
			v0 = v0+x
			paths.append(2)
		if v0 >= 7:
			v0 = x+8
			v0 = v0-1
			a1 = 4-a1
			paths.append(3)
		else:
			x = 2/a1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		v0 = a1**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))