import numpy as np 

def function(x):

	v9 = x
	g9 = x
	paths = []
	try:
		if g9 >= 3:
			g9 = g9+g9
			v9 = 5/g9
			x = x/x
			paths.append(1)
		else:
			v9 = 7+8
			v9 = v9/g9
			paths.append(2)
		if v9 > 1:
			v9 = v9-3
			paths.append(3)
		else:
			v9 = v9+v9
			x = g9/g9
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		v9 = g9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))