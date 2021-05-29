import numpy as np 

def function(x):

	g0 = x
	w6 = 9
	paths = []
	try:
		if w6 > 9:
			x = x-8
			w6 = 6+8
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if g0 > 6:
			x = x*3
			w6 = w6+8
			paths.append(3)
		else:
			x = 8*0
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		w6 = g0**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))