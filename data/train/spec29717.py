import numpy as np 

def function(x):

	g2 = x
	f1 = 5
	paths = []
	try:
		if f1 >= 9:
			f1 = 0/f1
			f1 = 9/f1
			paths.append(1)
		else:
			g2 = 0-g2
			g2 = g2+5
			g2 = x-g2
			paths.append(2)
		if f1 <= 1:
			x = x+7
			g2 = x+g2
			paths.append(3)
		else:
			x = x/8
			f1 = 8-f1
			g2 = g2+g2
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		f1 = g2**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))