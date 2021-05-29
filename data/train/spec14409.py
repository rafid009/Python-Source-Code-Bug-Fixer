import numpy as np 

def function(x):

	l1 = x
	d7 = x
	paths = []
	try:
		if l1 <= 0:
			x = x*1
			d7 = d7-d7
			paths.append(1)
		else:
			l1 = 1*l1
			d7 = d7-l1
			x = x*2
			paths.append(2)
		if l1 <= 9:
			x = x-d7
			paths.append(3)
		else:
			l1 = d7+x
			x = x*3
			d7 = 1*d7
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		d7 = l1**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))