import numpy as np 

def function(x):

	k0 = x
	j8 = x
	paths = []
	try:
		if x < 7:
			j8 = 2+j8
			x = x+x
			paths.append(1)
		else:
			x = j8+x
			x = 5+x
			paths.append(2)
		if k0 > 7:
			j8 = k0*j8
			k0 = 1-0
			x = 2-7
			paths.append(3)
		else:
			x = x+9
			x = x+4
			x = x+k0
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		j8 = k0**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))