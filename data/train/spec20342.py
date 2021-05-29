import numpy as np 

def function(x):

	i5 = x
	w9 = 6
	paths = []
	try:
		if x < 5:
			x = 9/i5
			w9 = w9+2
			i5 = 7+x
			paths.append(1)
		else:
			x = x+6
			i5 = 0+x
			paths.append(2)
		if i5 <= 4:
			i5 = 0+w9
			w9 = 4/9
			paths.append(3)
		else:
			x = 0-x
			x = 0*3
			i5 = i5+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))