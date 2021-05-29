import numpy as np 

def function(x):

	k0 = 8
	j8 = 4
	x = x
	paths = []
	try:
		if x > 5:
			x = x+2
			j8 = x/j8
			paths.append(1)
		else:
			k0 = 3-j8
			paths.append(2)
		if k0 <= 2:
			j8 = 7/j8
			x = x*j8
			x = x+6
			paths.append(3)
		else:
			x = 2+x
			x = j8/1
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		k0 = k0**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))