import numpy as np 

def function(x):

	d4 = x
	l3 = 3
	paths = []
	try:
		if l3 >= 3:
			l3 = 2*x
			x = x*l3
			x = x+9
			paths.append(1)
		else:
			d4 = 8+x
			paths.append(2)
		if l3 > 9:
			l3 = x+d4
			l3 = l3+7
			paths.append(3)
		else:
			d4 = 4/d4
			x = l3+2
			d4 = 8/d4
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		d4 = d4**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))