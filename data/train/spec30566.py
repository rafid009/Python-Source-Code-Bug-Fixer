import numpy as np 

def function(x):

	v3 = 1
	y4 = x
	paths = []
	try:
		if y4 >= 6:
			v3 = v3*x
			v3 = 2-v3
			y4 = x/v3
			paths.append(1)
		else:
			v3 = v3/9
			v3 = 4/2
			x = 4/x
			paths.append(2)
		if y4 >= 3:
			v3 = v3-y4
			x = x+x
			y4 = 2*y4
			paths.append(3)
		else:
			x = 5*x
			x = v3-6
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		y4 = v3**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))