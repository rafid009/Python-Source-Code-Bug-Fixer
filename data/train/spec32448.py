import numpy as np 

def function(x):

	p8 = x
	v2 = x
	paths = []
	try:
		if x > 1:
			p8 = 9+p8
			x = 0-x
			paths.append(1)
		else:
			p8 = 5-p8
			paths.append(2)
		if p8 > 7:
			x = 7*p8
			x = x+1
			paths.append(3)
		else:
			x = x-7
			v2 = v2+8
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		x = v2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))