import numpy as np 

def function(x):

	r7 = x
	k3 = 8
	paths = []
	try:
		if k3 <= 7:
			x = 4*0
			k3 = k3+6
			k3 = k3+3
			paths.append(1)
		else:
			r7 = 6/r7
			x = k3+x
			paths.append(2)
		if k3 <= 9:
			x = r7*x
			x = 3*x
			paths.append(3)
		else:
			x = x-8
			x = x*k3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k3 = x**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))