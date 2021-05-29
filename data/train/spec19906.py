import numpy as np 

def function(x):

	n1 = 3
	j0 = x
	x = 0
	paths = []
	try:
		if x < 7:
			j0 = 3-j0
			paths.append(1)
		else:
			n1 = n1+2
			n1 = n1*4
			x = x*7
			paths.append(2)
		if j0 >= 7:
			j0 = x+x
			paths.append(3)
		else:
			n1 = j0/n1
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		j0 = n1**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))