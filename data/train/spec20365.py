import numpy as np 

def function(x):

	n8 = x
	v2 = 3
	paths = []
	try:
		if x <= 9:
			x = x+x
			n8 = n8+4
			v2 = 7+x
			paths.append(1)
		else:
			v2 = v2/2
			v2 = v2-9
			x = n8+5
			paths.append(2)
		if x <= 7:
			x = 9-v2
			x = 4/x
			paths.append(3)
		else:
			x = 1+8
			x = 6*x
			v2 = 3*x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		x = v2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))