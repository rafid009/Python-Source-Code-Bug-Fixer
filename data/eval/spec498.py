import numpy as np 

def function(x):

	t5 = 1
	u2 = 4
	paths = []
	try:
		if u2 < 5:
			t5 = 0-t5
			t5 = 5-7
			x = x-8
			paths.append(1)
		else:
			t5 = 0/t5
			x = x/5
			paths.append(2)
		if u2 < 0:
			x = x/7
			t5 = u2+t5
			paths.append(3)
		else:
			u2 = 3+5
			t5 = t5/t5
			u2 = x/t5
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