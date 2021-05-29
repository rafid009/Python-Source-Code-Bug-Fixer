import numpy as np 

def function(x):

	n8 = x
	e1 = 1
	paths = []
	try:
		if x < 5:
			n8 = 4+n8
			x = 6*0
			n8 = n8-e1
			paths.append(1)
		else:
			x = 3-n8
			n8 = 0+n8
			n8 = 6-e1
			paths.append(2)
		if x > 8:
			e1 = x+9
			x = 5+x
			paths.append(3)
		else:
			n8 = 8*n8
			e1 = x/6
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		n8 = e1**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))