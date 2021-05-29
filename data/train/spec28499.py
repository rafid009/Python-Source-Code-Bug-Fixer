import numpy as np 

def function(x):

	k0 = x
	j2 = 2
	paths = []
	try:
		if j2 > 1:
			j2 = 4-j2
			j2 = 5*4
			x = 5-j2
			paths.append(1)
		else:
			x = x+j2
			paths.append(2)
		if k0 < 5:
			k0 = 6*k0
			j2 = x*j2
			paths.append(3)
		else:
			k0 = j2*k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))