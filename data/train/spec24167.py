import numpy as np 

def function(x):

	o4 = 7
	g4 = x
	paths = []
	try:
		if g4 <= 5:
			x = o4-8
			x = 9/4
			x = x/6
			paths.append(1)
		else:
			x = 2/4
			paths.append(2)
		if g4 >= 2:
			o4 = o4-1
			o4 = 9/o4
			x = x*8
			paths.append(3)
		else:
			o4 = x+9
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))