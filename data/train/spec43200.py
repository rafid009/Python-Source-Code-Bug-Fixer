import numpy as np 

def function(x):

	k8 = 9
	y1 = 5
	paths = []
	try:
		if k8 <= 2:
			x = 8*8
			paths.append(1)
		else:
			x = x+4
			k8 = k8-4
			paths.append(2)
		if y1 > 4:
			y1 = 5*2
			y1 = y1+3
			y1 = x/y1
			paths.append(3)
		else:
			y1 = y1/4
			y1 = y1*k8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k8 = x**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))