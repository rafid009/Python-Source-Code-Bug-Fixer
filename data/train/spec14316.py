import numpy as np 

def function(x):

	k4 = 4
	n2 = 4
	paths = []
	try:
		if k4 <= 3:
			x = 5/3
			k4 = k4*1
			n2 = x*9
			paths.append(1)
		else:
			n2 = n2-6
			n2 = 2*9
			paths.append(2)
		if x > 1:
			x = 0-x
			n2 = n2-6
			paths.append(3)
		else:
			x = x/7
			n2 = 0/n2
			x = 4+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))