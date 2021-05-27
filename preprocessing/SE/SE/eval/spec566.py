import numpy as np 

def function(x):

	u3 = 3
	l9 = x
	paths = []
	try:
		if u3 <= 8:
			x = x+x
			u3 = u3/u3
			u3 = 9+x
			paths.append(1)
		else:
			x = l9+5
			u3 = 8-2
			l9 = 6-l9
			paths.append(2)
		if x > 9:
			l9 = l9+0
			l9 = 3-l9
			paths.append(3)
		else:
			x = x/3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))