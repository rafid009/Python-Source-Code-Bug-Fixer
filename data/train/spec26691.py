import numpy as np 

def function(x):

	l5 = x
	a1 = x
	paths = []
	try:
		if l5 < 5:
			x = 8*x
			a1 = 9/8
			l5 = 6+l5
			paths.append(1)
		else:
			l5 = a1-x
			a1 = 7-a1
			paths.append(2)
		if l5 <= 6:
			a1 = l5+6
			x = x*2
			paths.append(3)
		else:
			x = 7-l5
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))