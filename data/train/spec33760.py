import numpy as np 

def function(x):

	r1 = 7
	k3 = 8
	paths = []
	try:
		if r1 > 9:
			r1 = 3+r1
			k3 = 4-k3
			paths.append(1)
		else:
			r1 = r1+2
			x = r1*4
			k3 = r1*9
			paths.append(2)
		if r1 >= 1:
			x = 9-x
			r1 = r1-3
			paths.append(3)
		else:
			r1 = r1*0
			k3 = k3/3
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