import numpy as np 

def function(x):

	b3 = x
	g2 = x
	paths = []
	try:
		if b3 > 0:
			x = x*2
			g2 = b3+g2
			x = b3/5
			paths.append(1)
		else:
			x = x-7
			b3 = b3+7
			g2 = g2-7
			paths.append(2)
		if b3 > 2:
			b3 = 2+b3
			paths.append(3)
		else:
			x = x*9
			x = 1*5
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		b3 = g2**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))