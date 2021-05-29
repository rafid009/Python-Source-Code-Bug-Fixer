import numpy as np 

def function(x):

	d5 = 7
	k8 = x
	paths = []
	try:
		if d5 < 9:
			k8 = k8*4
			paths.append(1)
		else:
			d5 = 7*8
			d5 = d5-8
			d5 = 9*d5
			paths.append(2)
		if x >= 4:
			d5 = d5+1
			x = x*2
			paths.append(3)
		else:
			k8 = x*x
			d5 = d5+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))