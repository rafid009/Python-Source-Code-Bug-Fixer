import numpy as np 

def function(x):

	v6 = 5
	f0 = 8
	paths = []
	try:
		if v6 >= 2:
			v6 = v6-f0
			x = x-f0
			paths.append(1)
		else:
			f0 = f0/2
			v6 = 9-x
			paths.append(2)
		if v6 <= 0:
			f0 = f0/7
			v6 = 4*x
			paths.append(3)
		else:
			x = 2*x
			f0 = f0-x
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