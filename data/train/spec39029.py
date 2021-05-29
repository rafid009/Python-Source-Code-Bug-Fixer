import numpy as np 

def function(x):

	g9 = 8
	d6 = 0
	paths = []
	try:
		if g9 <= 1:
			d6 = d6+4
			paths.append(1)
		else:
			x = x+8
			d6 = d6/9
			paths.append(2)
		if x < 5:
			x = 8+7
			g9 = 1-g9
			paths.append(3)
		else:
			x = 5-g9
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))