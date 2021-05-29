import numpy as np 

def function(x):

	p5 = 5
	n1 = x
	paths = []
	try:
		if x <= 0:
			n1 = x+9
			x = 4*9
			paths.append(1)
		else:
			x = 0-x
			n1 = n1*1
			paths.append(2)
		if p5 < 8:
			x = x/3
			p5 = n1-p5
			paths.append(3)
		else:
			x = 8*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))