import numpy as np 

def function(x):

	k3 = x
	v0 = x
	paths = []
	try:
		if k3 > 2:
			x = x/9
			paths.append(1)
		else:
			v0 = 4*v0
			x = 0*x
			k3 = k3+9
			paths.append(2)
		if x < 2:
			x = x*k3
			v0 = v0*9
			x = 9+1
			paths.append(3)
		else:
			v0 = v0+9
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x = v0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))