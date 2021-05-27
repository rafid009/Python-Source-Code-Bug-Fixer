import numpy as np 

def function(x):

	n8 = 4
	n9 = x
	paths = []
	try:
		if n8 <= 4:
			n8 = n8/n9
			paths.append(1)
		else:
			n9 = n9*8
			x = 2*1
			paths.append(2)
		if x < 1:
			x = 3*0
			n9 = n9*1
			paths.append(3)
		else:
			n8 = n8+x
			n9 = 1/x
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))