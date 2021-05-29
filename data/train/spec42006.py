import numpy as np 

def function(x):

	l9 = x
	d2 = 3
	paths = []
	try:
		if x > 7:
			x = 0/5
			l9 = x*d2
			d2 = d2-d2
			paths.append(1)
		else:
			x = d2+x
			x = 7+d2
			d2 = 1*d2
			paths.append(2)
		if x < 6:
			l9 = 1+l9
			paths.append(3)
		else:
			d2 = 3/1
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		d2 = l9**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))