import numpy as np 

def function(x):

	v3 = x
	n7 = 7
	paths = []
	try:
		if x >= 7:
			x = 9/x
			v3 = 6+n7
			x = x*9
			paths.append(1)
		else:
			v3 = 4*8
			v3 = 5*x
			n7 = n7/v3
			paths.append(2)
		if n7 <= 5:
			x = x/8
			paths.append(3)
		else:
			v3 = v3/8
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))