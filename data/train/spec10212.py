import numpy as np 

def function(x):

	j2 = x
	n0 = x
	paths = []
	try:
		if j2 > 4:
			x = 1*7
			j2 = n0-n0
			paths.append(1)
		else:
			n0 = x+9
			paths.append(2)
		if n0 > 7:
			j2 = j2*5
			paths.append(3)
		else:
			j2 = n0+n0
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		n0 = j2**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))