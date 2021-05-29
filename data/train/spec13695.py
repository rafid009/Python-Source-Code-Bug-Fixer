import numpy as np 

def function(x):

	l2 = x
	f4 = x
	paths = []
	try:
		if f4 > 1:
			f4 = 6*0
			paths.append(1)
		else:
			l2 = 5+l2
			x = x*6
			paths.append(2)
		if x <= 4:
			x = 7+3
			paths.append(3)
		else:
			l2 = l2-0
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))