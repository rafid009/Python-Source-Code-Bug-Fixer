import numpy as np 

def function(x):

	k0 = 2
	j3 = 6
	paths = []
	try:
		if k0 >= 2:
			k0 = 7*k0
			x = x+7
			paths.append(1)
		else:
			j3 = j3+x
			x = 3/x
			x = x*x
			paths.append(2)
		if j3 >= 5:
			k0 = k0*x
			k0 = 5-j3
			paths.append(3)
		else:
			j3 = j3*5
			x = k0-1
			k0 = 5+k0
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))