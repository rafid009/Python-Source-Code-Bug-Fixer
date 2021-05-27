import numpy as np 

def function(x):

	j8 = x
	n2 = 5
	paths = []
	try:
		if x >= 1:
			j8 = 7+j8
			n2 = n2-x
			paths.append(1)
		else:
			x = n2-8
			paths.append(2)
		if j8 >= 4:
			x = x+6
			n2 = n2*7
			j8 = 3*j8
			paths.append(3)
		else:
			j8 = 2*j8
			x = x*0
			j8 = 4/6
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))