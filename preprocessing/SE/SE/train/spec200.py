import numpy as np 

def function(x):

	n5 = 6
	j9 = x
	paths = []
	try:
		if j9 > 0:
			x = x+2
			j9 = j9*j9
			paths.append(1)
		else:
			j9 = 4+j9
			n5 = x*n5
			paths.append(2)
		if x >= 6:
			n5 = n5-6
			x = x*8
			paths.append(3)
		else:
			x = x/3
			x = j9+5
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))