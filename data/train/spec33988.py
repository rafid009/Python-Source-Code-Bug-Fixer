import numpy as np 

def function(x):

	z2 = x
	j2 = 8
	paths = []
	try:
		if j2 >= 8:
			x = x*1
			paths.append(1)
		else:
			z2 = z2*4
			j2 = z2*4
			x = 6+3
			paths.append(2)
		if z2 <= 6:
			x = j2+x
			j2 = j2-0
			x = 3-x
			paths.append(3)
		else:
			x = j2/x
			x = 3+6
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))