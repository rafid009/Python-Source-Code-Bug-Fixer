import numpy as np 

def function(x):

	n9 = 7
	j2 = 8
	paths = []
	try:
		if n9 <= 5:
			x = j2*1
			j2 = j2*n9
			j2 = 1+x
			paths.append(1)
		else:
			j2 = 9*j2
			paths.append(2)
		if j2 > 0:
			n9 = 9+x
			n9 = j2*j2
			n9 = x-8
			paths.append(3)
		else:
			x = 1+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))