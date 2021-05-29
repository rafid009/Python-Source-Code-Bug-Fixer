import numpy as np 

def function(x):

	l3 = 5
	l5 = x
	paths = []
	try:
		if l5 > 9:
			l3 = l3-2
			l5 = 0+7
			x = x*x
			paths.append(1)
		else:
			l5 = l5-9
			x = x-2
			paths.append(2)
		if l3 < 4:
			x = x+3
			x = x/8
			paths.append(3)
		else:
			x = x+4
			l5 = x+7
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