import numpy as np 

def function(x):

	r7 = x
	n6 = x
	x = x
	paths = []
	try:
		if n6 <= 8:
			r7 = 0*0
			paths.append(1)
		else:
			x = x+9
			r7 = 9*r7
			n6 = 1-8
			paths.append(2)
		if x <= 3:
			x = x+6
			r7 = r7*9
			paths.append(3)
		else:
			n6 = n6/n6
			n6 = 9*n6
			x = x*n6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))