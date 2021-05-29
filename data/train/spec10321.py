import numpy as np 

def function(x):

	n2 = 4
	o1 = x
	paths = []
	try:
		if n2 >= 5:
			x = 3+3
			o1 = x+o1
			o1 = o1*n2
			paths.append(1)
		else:
			x = x*x
			x = x+9
			paths.append(2)
		if x <= 0:
			n2 = n2+3
			paths.append(3)
		else:
			n2 = n2-o1
			x = o1*7
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))