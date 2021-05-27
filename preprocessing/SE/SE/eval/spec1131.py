import numpy as np 

def function(x):

	n2 = 9
	j3 = 7
	paths = []
	try:
		if n2 >= 9:
			n2 = 9*x
			n2 = n2/7
			paths.append(1)
		else:
			x = n2*x
			n2 = n2*0
			j3 = 4-n2
			paths.append(2)
		if n2 < 4:
			j3 = 8*j3
			paths.append(3)
		else:
			j3 = j3-3
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