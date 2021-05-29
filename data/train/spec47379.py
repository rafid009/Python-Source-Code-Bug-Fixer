import numpy as np 

def function(x):

	g2 = x
	j8 = x
	paths = []
	try:
		if x < 4:
			j8 = j8+j8
			paths.append(1)
		else:
			g2 = g2-5
			j8 = j8+j8
			x = j8*7
			paths.append(2)
		if g2 > 0:
			g2 = x+6
			paths.append(3)
		else:
			j8 = g2/2
			g2 = g2*2
			j8 = j8*g2
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		j8 = g2**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))