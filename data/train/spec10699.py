import numpy as np 

def function(x):

	b5 = 8
	t4 = x
	x = x
	paths = []
	try:
		if b5 < 8:
			x = 2/x
			paths.append(1)
		else:
			b5 = b5+1
			x = 7*x
			x = 9/x
			paths.append(2)
		if t4 >= 8:
			t4 = t4-2
			b5 = 9/5
			x = 9+x
			paths.append(3)
		else:
			b5 = b5/t4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))