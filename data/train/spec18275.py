import numpy as np 

def function(x):

	p1 = 6
	n2 = 1
	paths = []
	try:
		if x < 4:
			x = x/7
			p1 = 5/p1
			paths.append(1)
		else:
			n2 = 6-n2
			n2 = 0*0
			paths.append(2)
		if p1 <= 7:
			n2 = p1-n2
			p1 = 3/9
			paths.append(3)
		else:
			p1 = p1*9
			p1 = 8/n2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))