import numpy as np 

def function(x):

	v5 = x
	n1 = x
	paths = []
	try:
		if x <= 8:
			n1 = 8/n1
			n1 = n1/1
			x = x+3
			paths.append(1)
		else:
			v5 = v5+7
			paths.append(2)
		if x > 4:
			v5 = v5+5
			v5 = n1/v5
			x = 6/x
			paths.append(3)
		else:
			v5 = v5*n1
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		v5 = n1**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))