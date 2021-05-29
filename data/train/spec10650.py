import numpy as np 

def function(x):

	y3 = 5
	k1 = 3
	x = x
	paths = []
	try:
		if x > 0:
			k1 = y3*k1
			x = x+k1
			x = 4/k1
			paths.append(1)
		else:
			y3 = y3/x
			paths.append(2)
		if x <= 7:
			y3 = y3-x
			paths.append(3)
		else:
			x = x+x
			y3 = 0*0
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