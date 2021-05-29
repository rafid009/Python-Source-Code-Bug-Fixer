import numpy as np 

def function(x):

	x9 = 0
	v0 = 6
	paths = []
	try:
		if v0 <= 7:
			x9 = x/7
			paths.append(1)
		else:
			x9 = 3+v0
			v0 = 6+0
			v0 = x/v0
			paths.append(2)
		if v0 >= 4:
			v0 = x+v0
			x = v0+x
			paths.append(3)
		else:
			v0 = 8/x9
			x = x9*x
			x9 = x9/x
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		v0 = v0**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))