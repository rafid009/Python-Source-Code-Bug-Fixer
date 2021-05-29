import numpy as np 

def function(x):

	j6 = 2
	l6 = x
	paths = []
	try:
		if x <= 5:
			l6 = l6-3
			l6 = 4*x
			paths.append(1)
		else:
			l6 = 4*1
			paths.append(2)
		if l6 >= 9:
			x = j6*x
			x = x+x
			paths.append(3)
		else:
			x = x+3
			l6 = l6+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))