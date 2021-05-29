import numpy as np 

def function(x):

	k3 = 3
	a7 = x
	paths = []
	try:
		if a7 >= 0:
			k3 = x*k3
			x = 4+3
			paths.append(1)
		else:
			k3 = k3+5
			a7 = 5*6
			paths.append(2)
		if k3 <= 4:
			a7 = 6/2
			a7 = 7+9
			k3 = x+7
			paths.append(3)
		else:
			a7 = x+0
			x = 2-x
			a7 = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))