import numpy as np 

def function(x):

	o0 = 7
	g9 = 4
	paths = []
	try:
		if o0 > 0:
			g9 = g9+x
			o0 = o0-6
			g9 = 0-8
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if o0 < 1:
			g9 = 0+g9
			x = 6+x
			paths.append(3)
		else:
			g9 = g9*x
			o0 = 1*o0
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		o0 = g9**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))