import numpy as np 

def function(x):

	n1 = 6
	v7 = x
	paths = []
	try:
		if v7 > 7:
			x = x*x
			x = 9-v7
			x = 0/x
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if x < 0:
			x = x+7
			n1 = v7+0
			n1 = n1*0
			paths.append(3)
		else:
			x = x-0
			x = n1*n1
			n1 = v7*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))