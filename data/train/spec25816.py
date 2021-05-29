import numpy as np 

def function(x):

	w2 = 4
	j8 = 9
	paths = []
	try:
		if j8 <= 1:
			x = x*x
			paths.append(1)
		else:
			x = j8*x
			paths.append(2)
		if j8 >= 8:
			w2 = w2-7
			x = 7+x
			paths.append(3)
		else:
			x = 3-x
			j8 = j8+6
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		x = w2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))