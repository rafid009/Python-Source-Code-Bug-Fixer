import numpy as np 

def function(x):

	l1 = 2
	d5 = x
	paths = []
	try:
		if d5 <= 4:
			l1 = 4+9
			x = 0+8
			paths.append(1)
		else:
			d5 = x+l1
			l1 = l1*2
			l1 = 3-l1
			paths.append(2)
		if x >= 4:
			d5 = d5*8
			d5 = l1+d5
			paths.append(3)
		else:
			l1 = l1-5
			d5 = d5*d5
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		d5 = l1**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))