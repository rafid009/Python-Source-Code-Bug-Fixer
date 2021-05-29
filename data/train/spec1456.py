import numpy as np 

def function(x):

	n1 = 4
	i0 = x
	paths = []
	try:
		if n1 <= 8:
			n1 = 2-1
			paths.append(1)
		else:
			x = x+n1
			i0 = i0*0
			paths.append(2)
		if i0 >= 3:
			n1 = n1/n1
			x = x+x
			paths.append(3)
		else:
			n1 = n1*3
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		n1 = i0**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))