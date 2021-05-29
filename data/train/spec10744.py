import numpy as np 

def function(x):

	y2 = x
	l5 = 7
	paths = []
	try:
		if l5 < 3:
			l5 = l5-9
			paths.append(1)
		else:
			x = x/l5
			x = x-x
			x = x-8
			paths.append(2)
		if l5 > 5:
			x = x+y2
			y2 = y2+7
			l5 = 2+l5
			paths.append(3)
		else:
			y2 = x*0
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))