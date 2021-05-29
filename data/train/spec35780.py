import numpy as np 

def function(x):

	p2 = 0
	d2 = 7
	paths = []
	try:
		if x >= 4:
			x = 3+x
			d2 = d2/1
			x = x/9
			paths.append(1)
		else:
			d2 = 9*d2
			p2 = 1+p2
			paths.append(2)
		if d2 < 4:
			d2 = 4+1
			d2 = x*5
			paths.append(3)
		else:
			d2 = d2-9
			p2 = 5+9
			p2 = p2+2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))