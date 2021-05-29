import numpy as np 

def function(x):

	l9 = x
	d9 = 6
	paths = []
	try:
		if l9 < 5:
			x = x/5
			x = 1-1
			d9 = x*d9
			paths.append(1)
		else:
			x = 2*3
			l9 = l9/4
			d9 = 8*d9
			paths.append(2)
		if x < 7:
			x = x/6
			x = x+x
			d9 = 8+3
			paths.append(3)
		else:
			x = x-d9
			x = x+d9
			d9 = d9*3
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))