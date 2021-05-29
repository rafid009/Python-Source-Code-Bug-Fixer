import numpy as np 

def function(x):

	r5 = x
	p2 = 2
	paths = []
	try:
		if r5 > 8:
			x = 6/4
			paths.append(1)
		else:
			x = 6+4
			p2 = 7/p2
			x = x/p2
			paths.append(2)
		if r5 <= 2:
			x = p2+2
			p2 = p2/r5
			paths.append(3)
		else:
			x = x/7
			p2 = 2*2
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))