import numpy as np 

def function(x):

	p1 = x
	n9 = x
	paths = []
	try:
		if n9 >= 7:
			p1 = p1*0
			paths.append(1)
		else:
			x = x-4
			p1 = p1+0
			paths.append(2)
		if n9 <= 3:
			p1 = p1-4
			paths.append(3)
		else:
			n9 = n9/5
			p1 = x/3
			x = 0+7
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