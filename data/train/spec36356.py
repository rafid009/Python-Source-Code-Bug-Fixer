import numpy as np 

def function(x):

	r1 = 1
	k3 = x
	paths = []
	try:
		if k3 >= 9:
			x = x*2
			x = r1-x
			k3 = x*6
			paths.append(1)
		else:
			k3 = x+k3
			paths.append(2)
		if x >= 6:
			x = x-7
			k3 = x/r1
			r1 = r1+4
			paths.append(3)
		else:
			x = 5-1
			x = k3*2
			k3 = 2-5
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		k3 = k3**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))