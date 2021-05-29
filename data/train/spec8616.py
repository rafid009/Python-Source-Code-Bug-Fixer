import numpy as np 

def function(x):

	k3 = 4
	y4 = 4
	paths = []
	try:
		if y4 >= 5:
			x = x+7
			x = 0*x
			k3 = y4/k3
			paths.append(1)
		else:
			y4 = y4-8
			y4 = 3-y4
			paths.append(2)
		if k3 > 2:
			k3 = k3*x
			paths.append(3)
		else:
			k3 = k3*0
			y4 = k3/1
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		y4 = k3**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))