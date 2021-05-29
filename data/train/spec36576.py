import numpy as np 

def function(x):

	g0 = 9
	f3 = 1
	paths = []
	try:
		if g0 <= 1:
			x = 0*f3
			x = 2*f3
			paths.append(1)
		else:
			x = 2-x
			g0 = x*g0
			paths.append(2)
		if f3 < 7:
			f3 = f3-4
			paths.append(3)
		else:
			f3 = f3/5
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		f3 = g0**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))