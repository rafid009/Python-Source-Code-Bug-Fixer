import numpy as np 

def function(x):

	g2 = 5
	v9 = 8
	paths = []
	try:
		if x > 2:
			v9 = 2-v9
			paths.append(1)
		else:
			x = x/v9
			paths.append(2)
		if g2 <= 2:
			g2 = v9-g2
			paths.append(3)
		else:
			v9 = 1/v9
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		v9 = v9**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))