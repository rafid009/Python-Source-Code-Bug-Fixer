import numpy as np 

def function(x):

	o9 = 8
	l9 = 1
	paths = []
	try:
		if x < 0:
			o9 = 3/x
			x = x*o9
			x = o9*0
			paths.append(1)
		else:
			x = 6/6
			paths.append(2)
		if o9 <= 9:
			l9 = l9-2
			x = x/6
			paths.append(3)
		else:
			l9 = l9*6
			o9 = o9*x
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