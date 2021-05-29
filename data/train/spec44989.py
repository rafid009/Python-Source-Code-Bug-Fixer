import numpy as np 

def function(x):

	r2 = x
	g9 = x
	paths = []
	try:
		if r2 >= 8:
			x = x-7
			paths.append(1)
		else:
			r2 = 4/7
			g9 = r2*g9
			paths.append(2)
		if r2 < 9:
			x = 0*x
			paths.append(3)
		else:
			r2 = r2/1
			x = g9+x
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