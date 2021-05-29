import numpy as np 

def function(x):

	f0 = 6
	k3 = x
	paths = []
	try:
		if k3 > 7:
			f0 = 1-5
			paths.append(1)
		else:
			k3 = 2+k3
			paths.append(2)
		if f0 >= 3:
			k3 = 4/9
			k3 = 5*k3
			paths.append(3)
		else:
			x = 5+x
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))