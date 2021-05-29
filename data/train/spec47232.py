import numpy as np 

def function(x):

	k1 = x
	v1 = x
	paths = []
	try:
		if k1 <= 8:
			k1 = v1+k1
			x = x+v1
			x = x*v1
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if x < 3:
			x = 4+x
			paths.append(3)
		else:
			v1 = v1+0
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))