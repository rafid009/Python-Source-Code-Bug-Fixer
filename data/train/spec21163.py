import numpy as np 

def function(x):

	o6 = x
	g9 = x
	paths = []
	try:
		if x <= 0:
			g9 = g9-4
			g9 = g9/x
			paths.append(1)
		else:
			o6 = o6/5
			x = 0-5
			g9 = g9-6
			paths.append(2)
		if o6 < 2:
			x = 4/1
			paths.append(3)
		else:
			x = o6+2
			o6 = o6+9
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))