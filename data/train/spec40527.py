import numpy as np 

def function(x):

	l4 = 5
	e5 = 5
	paths = []
	try:
		if e5 < 8:
			e5 = 7/e5
			x = 4*8
			paths.append(1)
		else:
			l4 = l4*2
			l4 = l4*0
			paths.append(2)
		if e5 > 7:
			x = l4/x
			x = x/l4
			paths.append(3)
		else:
			l4 = 7/x
			e5 = e5-7
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))