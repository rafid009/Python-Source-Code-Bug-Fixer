import numpy as np 

def function(x):

	r7 = 8
	t6 = 6
	paths = []
	try:
		if r7 < 9:
			r7 = r7-t6
			t6 = 1-1
			t6 = t6-0
			paths.append(1)
		else:
			r7 = r7-r7
			x = 5*x
			x = 6+x
			paths.append(2)
		if t6 > 4:
			t6 = t6+3
			x = x/9
			paths.append(3)
		else:
			x = x/8
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