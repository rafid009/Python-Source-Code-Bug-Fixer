import numpy as np 

def function(x):

	f3 = 3
	l5 = x
	paths = []
	try:
		if x > 6:
			x = l5+5
			x = x+4
			f3 = 2*l5
			paths.append(1)
		else:
			f3 = 4/f3
			f3 = f3+f3
			x = x-0
			paths.append(2)
		if f3 > 5:
			f3 = f3/6
			l5 = 5/5
			paths.append(3)
		else:
			x = 4+f3
			l5 = f3-x
			x = l5*4
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))