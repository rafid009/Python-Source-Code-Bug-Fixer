import numpy as np 

def function(x):

	v1 = x
	g9 = x
	paths = []
	try:
		if g9 <= 3:
			v1 = 1-6
			v1 = v1-5
			paths.append(1)
		else:
			x = x+2
			g9 = g9-g9
			x = 1-x
			paths.append(2)
		if v1 < 5:
			v1 = x/v1
			paths.append(3)
		else:
			x = x+g9
			g9 = 1+3
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))