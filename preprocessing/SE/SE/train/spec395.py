import numpy as np 

def function(x):

	g2 = 5
	n8 = 7
	paths = []
	try:
		if x < 2:
			n8 = n8+1
			paths.append(1)
		else:
			n8 = g2+x
			g2 = g2/5
			paths.append(2)
		if n8 >= 1:
			g2 = n8-8
			x = x+0
			paths.append(3)
		else:
			n8 = n8+1
			g2 = 2+g2
			g2 = g2-4
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		n8 = g2**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))