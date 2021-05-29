import numpy as np 

def function(x):

	i3 = 9
	k1 = 3
	x = x
	paths = []
	try:
		if k1 > 3:
			k1 = 4-1
			paths.append(1)
		else:
			i3 = 6*x
			paths.append(2)
		if k1 < 6:
			x = x*2
			k1 = k1+i3
			paths.append(3)
		else:
			i3 = i3*2
			k1 = 2-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))