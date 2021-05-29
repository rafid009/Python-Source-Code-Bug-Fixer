import numpy as np 

def function(x):

	d1 = 6
	l9 = 6
	paths = []
	try:
		if x <= 9:
			d1 = d1-7
			x = 6*x
			l9 = l9/1
			paths.append(1)
		else:
			d1 = x+5
			paths.append(2)
		if d1 < 8:
			l9 = d1-l9
			d1 = d1+3
			x = x-l9
			paths.append(3)
		else:
			d1 = 6*l9
			x = 3-d1
			x = x*0
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		d1 = l9**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))