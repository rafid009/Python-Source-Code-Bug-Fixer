import numpy as np 

def function(x):

	n2 = x
	p9 = x
	paths = []
	try:
		if x <= 3:
			x = x*6
			n2 = 6/x
			paths.append(1)
		else:
			x = 2+p9
			x = 2-n2
			n2 = 1*2
			paths.append(2)
		if p9 < 1:
			x = x/n2
			x = n2-x
			paths.append(3)
		else:
			p9 = 5+8
			n2 = 4/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))