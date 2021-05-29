import numpy as np 

def function(x):

	b3 = 3
	g1 = x
	x = 5
	paths = []
	try:
		if b3 >= 9:
			x = 5+8
			paths.append(1)
		else:
			g1 = g1-0
			paths.append(2)
		if b3 > 3:
			b3 = g1*2
			x = 0+5
			b3 = b3*g1
			paths.append(3)
		else:
			g1 = g1-7
			b3 = 3/9
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		b3 = g1**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))