import numpy as np 

def function(x):

	t3 = 5
	v8 = 2
	paths = []
	try:
		if x > 1:
			x = x+v8
			t3 = 1+7
			paths.append(1)
		else:
			v8 = v8+t3
			t3 = t3*7
			paths.append(2)
		if t3 <= 5:
			t3 = t3*8
			paths.append(3)
		else:
			v8 = x+v8
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