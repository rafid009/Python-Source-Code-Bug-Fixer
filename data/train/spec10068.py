import numpy as np 

def function(x):

	a0 = 3
	v0 = 7
	paths = []
	try:
		if a0 > 7:
			v0 = x*v0
			v0 = v0*3
			x = 8-a0
			paths.append(1)
		else:
			x = 5/x
			v0 = 8/v0
			v0 = v0-x
			paths.append(2)
		if v0 <= 9:
			x = 8-x
			x = 2+x
			paths.append(3)
		else:
			a0 = 2+v0
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		a0 = v0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))