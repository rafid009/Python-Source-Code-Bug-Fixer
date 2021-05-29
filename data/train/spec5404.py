import numpy as np 

def function(x):

	r8 = 8
	k3 = x
	paths = []
	try:
		if r8 <= 8:
			r8 = r8*7
			x = r8-5
			paths.append(1)
		else:
			k3 = r8*k3
			k3 = 4/r8
			paths.append(2)
		if r8 > 1:
			x = 6/x
			r8 = r8*r8
			paths.append(3)
		else:
			k3 = 5*5
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		r8 = k3**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))