import numpy as np 

def function(x):

	d9 = 0
	l1 = x
	paths = []
	try:
		if l1 > 0:
			l1 = 0*0
			d9 = d9*l1
			d9 = 9*8
			paths.append(1)
		else:
			x = x/5
			d9 = 6-9
			paths.append(2)
		if d9 >= 6:
			l1 = 1+l1
			l1 = l1*9
			x = d9*4
			paths.append(3)
		else:
			d9 = d9-d9
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		x = l1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))