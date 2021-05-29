import numpy as np 

def function(x):

	g2 = x
	v6 = 1
	paths = []
	try:
		if g2 > 4:
			v6 = 5-0
			v6 = 8/3
			paths.append(1)
		else:
			x = 8/x
			x = x/2
			x = 4/5
			paths.append(2)
		if g2 > 0:
			g2 = g2+g2
			g2 = g2/v6
			g2 = g2*v6
			paths.append(3)
		else:
			v6 = v6*v6
			v6 = g2+x
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))