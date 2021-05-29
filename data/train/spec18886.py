import numpy as np 

def function(x):

	r2 = x
	g9 = 6
	paths = []
	try:
		if r2 >= 7:
			r2 = r2/7
			g9 = g9-x
			paths.append(1)
		else:
			r2 = r2+6
			r2 = 3-6
			paths.append(2)
		if x > 2:
			r2 = 2+r2
			x = x+7
			paths.append(3)
		else:
			g9 = g9+6
			r2 = x+5
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		r2 = g9**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))