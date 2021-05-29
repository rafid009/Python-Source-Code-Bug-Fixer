import numpy as np 

def function(x):

	n2 = 0
	n9 = x
	paths = []
	try:
		if n2 < 3:
			n2 = 6+2
			paths.append(1)
		else:
			x = x*2
			n9 = n2+4
			n2 = n2+2
			paths.append(2)
		if x < 9:
			n2 = n2+0
			paths.append(3)
		else:
			n2 = 8/n2
			n2 = 5-n2
			x = x*n9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))