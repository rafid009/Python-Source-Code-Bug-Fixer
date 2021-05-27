import numpy as np 

def function(x):

	t4 = 9
	u3 = 4
	paths = []
	try:
		if x < 1:
			x = x/9
			paths.append(1)
		else:
			u3 = u3/9
			u3 = u3-3
			paths.append(2)
		if x > 8:
			x = 0*x
			t4 = t4/2
			u3 = u3/8
			paths.append(3)
		else:
			t4 = t4*1
			u3 = 0/2
			u3 = t4-4
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