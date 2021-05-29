import numpy as np 

def function(x):

	b5 = 7
	g9 = x
	paths = []
	try:
		if g9 >= 7:
			g9 = 0-g9
			paths.append(1)
		else:
			g9 = g9*0
			b5 = b5+b5
			paths.append(2)
		if x < 8:
			g9 = g9-8
			paths.append(3)
		else:
			b5 = 6*b5
			x = g9*9
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		b5 = g9**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))