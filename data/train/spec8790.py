import numpy as np 

def function(x):

	y9 = x
	i3 = x
	paths = []
	try:
		if i3 < 9:
			x = 3*x
			x = y9*i3
			paths.append(1)
		else:
			x = x-4
			y9 = y9*0
			y9 = y9-x
			paths.append(2)
		if i3 < 3:
			i3 = 5*i3
			y9 = i3-y9
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		y9 = y9**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))