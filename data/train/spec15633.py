import numpy as np 

def function(x):

	v7 = 0
	n3 = x
	paths = []
	try:
		if v7 > 9:
			v7 = 3*0
			n3 = 7+n3
			x = x-v7
			paths.append(1)
		else:
			v7 = 2*x
			n3 = n3-8
			x = 5/x
			paths.append(2)
		if n3 <= 9:
			n3 = 3+9
			x = x-n3
			paths.append(3)
		else:
			n3 = 8-n3
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))