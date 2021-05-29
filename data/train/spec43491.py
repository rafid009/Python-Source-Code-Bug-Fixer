import numpy as np 

def function(x):

	v4 = x
	l9 = x
	paths = []
	try:
		if v4 <= 1:
			x = x*9
			x = 3/x
			v4 = 6+l9
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if l9 > 2:
			x = 1*x
			paths.append(3)
		else:
			l9 = l9*0
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		l9 = v4**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))