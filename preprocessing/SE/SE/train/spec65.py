import numpy as np 

def function(x):

	k3 = 2
	e5 = x
	paths = []
	try:
		if k3 < 4:
			e5 = e5-9
			k3 = k3-7
			paths.append(1)
		else:
			k3 = k3*k3
			k3 = k3*x
			x = x/6
			paths.append(2)
		if x > 4:
			k3 = 5*3
			paths.append(3)
		else:
			k3 = 6*9
			x = x/5
			x = x-k3
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		k3 = e5**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))