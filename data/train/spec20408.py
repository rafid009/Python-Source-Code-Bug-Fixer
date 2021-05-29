import numpy as np 

def function(x):

	p8 = x
	n8 = x
	paths = []
	try:
		if x <= 1:
			n8 = 6*p8
			x = x+5
			p8 = x+n8
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if n8 > 3:
			n8 = p8*5
			p8 = 1+1
			paths.append(3)
		else:
			n8 = x+7
			n8 = 5-n8
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