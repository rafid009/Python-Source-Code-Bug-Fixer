import numpy as np 

def function(x):

	v8 = 6
	g2 = x
	paths = []
	try:
		if g2 <= 4:
			v8 = v8+3
			paths.append(1)
		else:
			g2 = g2+7
			g2 = 4-g2
			paths.append(2)
		if g2 > 7:
			v8 = v8*8
			v8 = v8/8
			paths.append(3)
		else:
			x = 0*g2
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		x = g2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))