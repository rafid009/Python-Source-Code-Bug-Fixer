import numpy as np 

def function(x):

	n1 = 4
	v6 = x
	x = x
	paths = []
	try:
		if x <= 5:
			v6 = v6+6
			x = x-6
			paths.append(1)
		else:
			n1 = 7+n1
			x = 4/x
			n1 = n1-5
			paths.append(2)
		if v6 <= 5:
			n1 = n1-5
			v6 = 2+v6
			v6 = 4*9
			paths.append(3)
		else:
			v6 = v6/9
			n1 = 0-n1
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))