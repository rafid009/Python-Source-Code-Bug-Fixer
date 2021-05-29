import numpy as np 

def function(x):

	g3 = x
	v6 = 1
	paths = []
	try:
		if v6 < 9:
			g3 = g3+v6
			x = 1*9
			v6 = v6/x
			paths.append(1)
		else:
			v6 = 7-v6
			paths.append(2)
		if x <= 0:
			x = x-v6
			paths.append(3)
		else:
			x = x/3
			x = v6/8
			v6 = g3*v6
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))