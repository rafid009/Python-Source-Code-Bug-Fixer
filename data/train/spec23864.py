import numpy as np 

def function(x):

	n2 = 5
	a3 = 7
	paths = []
	try:
		if x < 1:
			x = 1+x
			paths.append(1)
		else:
			x = x-a3
			n2 = 8+n2
			paths.append(2)
		if x <= 7:
			x = x+a3
			x = x+x
			n2 = n2+x
			paths.append(3)
		else:
			n2 = n2*2
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		a3 = n2**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))