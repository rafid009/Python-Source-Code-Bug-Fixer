import numpy as np 

def function(x):

	t6 = x
	n2 = 5
	paths = []
	try:
		if n2 >= 3:
			n2 = n2/6
			t6 = t6-n2
			paths.append(1)
		else:
			n2 = 7+n2
			x = 0+9
			paths.append(2)
		if n2 < 8:
			n2 = x*x
			x = x+4
			paths.append(3)
		else:
			t6 = n2-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))