import numpy as np 

def function(x):

	n5 = 9
	v9 = x
	x = 2
	paths = []
	try:
		if v9 >= 0:
			v9 = 7*v9
			paths.append(1)
		else:
			x = x/2
			v9 = v9/x
			paths.append(2)
		if v9 >= 0:
			x = x+1
			paths.append(3)
		else:
			n5 = 7/n5
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))