import numpy as np 

def function(x):

	a2 = x
	f0 = x
	x = 2
	paths = []
	try:
		if x < 4:
			a2 = a2+8
			paths.append(1)
		else:
			f0 = 2+9
			paths.append(2)
		if a2 < 7:
			x = 9/x
			x = 4/2
			a2 = 4-a2
			paths.append(3)
		else:
			x = 2+a2
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))