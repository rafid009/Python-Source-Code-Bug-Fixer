import numpy as np 

def function(x):

	v3 = 5
	z2 = x
	paths = []
	try:
		if v3 > 6:
			v3 = 1/x
			v3 = z2*v3
			paths.append(1)
		else:
			v3 = z2+9
			v3 = x/2
			v3 = v3*z2
			paths.append(2)
		if z2 >= 5:
			v3 = 9*v3
			paths.append(3)
		else:
			x = x/x
			v3 = 0-v3
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))