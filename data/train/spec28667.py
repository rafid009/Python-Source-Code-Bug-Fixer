import numpy as np 

def function(x):

	b1 = 8
	g2 = x
	paths = []
	try:
		if x <= 9:
			x = g2+b1
			paths.append(1)
		else:
			b1 = b1-b1
			paths.append(2)
		if x <= 8:
			b1 = 5-9
			paths.append(3)
		else:
			x = 8+x
			x = x/4
			b1 = 4/g2
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		b1 = g2**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))