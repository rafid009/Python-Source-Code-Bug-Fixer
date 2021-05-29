import numpy as np 

def function(x):

	g9 = x
	t5 = x
	x = 6
	paths = []
	try:
		if x > 6:
			x = 4/x
			paths.append(1)
		else:
			x = g9-g9
			x = x*6
			x = x+t5
			paths.append(2)
		if x >= 0:
			x = t5-8
			x = 7+x
			g9 = 8+5
			paths.append(3)
		else:
			g9 = g9/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))