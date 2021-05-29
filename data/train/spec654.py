import numpy as np 

def function(x):

	w5 = 2
	t7 = x
	paths = []
	try:
		if t7 < 7:
			x = x*2
			x = x/x
			paths.append(1)
		else:
			w5 = 3*9
			t7 = 4*w5
			paths.append(2)
		if x < 7:
			t7 = t7/8
			x = 5+x
			paths.append(3)
		else:
			x = w5*x
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))