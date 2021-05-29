import numpy as np 

def function(x):

	l9 = 8
	x5 = x
	x = 0
	paths = []
	try:
		if l9 < 3:
			x5 = x-3
			paths.append(1)
		else:
			x = x5-5
			l9 = 8+9
			x5 = 5-6
			paths.append(2)
		if l9 > 1:
			x = x/3
			x = 6*0
			x = 1-x
			paths.append(3)
		else:
			x5 = x5*3
			l9 = 7*l9
			l9 = 3-l9
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		l9 = x5**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))