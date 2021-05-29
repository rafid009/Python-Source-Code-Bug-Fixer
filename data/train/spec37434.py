import numpy as np 

def function(x):

	z2 = 5
	v1 = x
	paths = []
	try:
		if z2 <= 0:
			x = v1/x
			v1 = 7+v1
			paths.append(1)
		else:
			x = x*3
			x = x-7
			x = x+x
			paths.append(2)
		if z2 >= 8:
			x = 2/4
			paths.append(3)
		else:
			v1 = x*z2
			v1 = v1+4
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))