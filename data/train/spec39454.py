import numpy as np 

def function(x):

	l5 = x
	e8 = 6
	paths = []
	try:
		if e8 < 9:
			x = 6*2
			l5 = l5-1
			paths.append(1)
		else:
			l5 = l5-0
			e8 = 6-e8
			e8 = e8/l5
			paths.append(2)
		if e8 > 3:
			e8 = e8-3
			e8 = 5-6
			e8 = l5/e8
			paths.append(3)
		else:
			x = 4/2
			e8 = 3-8
			l5 = l5+x
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