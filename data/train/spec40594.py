import numpy as np 

def function(x):

	o9 = x
	l9 = 9
	x = 2
	paths = []
	try:
		if x < 2:
			o9 = o9-l9
			paths.append(1)
		else:
			l9 = 2/l9
			x = x+x
			paths.append(2)
		if l9 <= 1:
			x = x*7
			paths.append(3)
		else:
			o9 = 4-o9
			l9 = 8+l9
			x = l9+x
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		l9 = o9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))