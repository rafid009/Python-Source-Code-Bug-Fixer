import numpy as np 

def function(x):

	z1 = x
	u6 = x
	paths = []
	try:
		if x >= 3:
			x = u6/x
			paths.append(1)
		else:
			u6 = u6*0
			paths.append(2)
		if x < 5:
			u6 = u6-6
			paths.append(3)
		else:
			u6 = 4+x
			z1 = 4+1
			x = x*7
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))