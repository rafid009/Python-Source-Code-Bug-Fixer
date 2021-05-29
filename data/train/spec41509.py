import numpy as np 

def function(x):

	d1 = x
	p7 = 6
	paths = []
	try:
		if x >= 7:
			p7 = p7-d1
			x = x/1
			paths.append(1)
		else:
			p7 = p7-x
			d1 = d1*0
			d1 = 8-d1
			paths.append(2)
		if d1 < 6:
			x = 1+x
			paths.append(3)
		else:
			p7 = 2*1
			p7 = p7-d1
			d1 = 5*d1
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		d1 = p7**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))