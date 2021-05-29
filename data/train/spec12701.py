import numpy as np 

def function(x):

	w3 = x
	p2 = x
	paths = []
	try:
		if x <= 6:
			w3 = w3/x
			p2 = p2-1
			w3 = p2+x
			paths.append(1)
		else:
			p2 = p2*4
			p2 = 9*w3
			paths.append(2)
		if p2 <= 5:
			x = 7/x
			paths.append(3)
		else:
			x = p2/x
			w3 = w3-0
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))