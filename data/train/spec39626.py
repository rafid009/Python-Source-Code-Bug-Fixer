import numpy as np 

def function(x):

	f9 = x
	k3 = x
	x = 6
	paths = []
	try:
		if x >= 8:
			x = 3-x
			k3 = k3-k3
			k3 = 9-k3
			paths.append(1)
		else:
			x = x*k3
			x = 4/x
			x = x-5
			paths.append(2)
		if x < 9:
			f9 = x/3
			paths.append(3)
		else:
			f9 = f9+1
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))