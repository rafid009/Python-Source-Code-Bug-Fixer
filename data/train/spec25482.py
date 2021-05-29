import numpy as np 

def function(x):

	i6 = x
	t4 = x
	paths = []
	try:
		if t4 <= 9:
			t4 = 2*3
			x = x-2
			x = 9+x
			paths.append(1)
		else:
			x = x/7
			t4 = i6*t4
			paths.append(2)
		if i6 < 0:
			t4 = t4+3
			x = x+7
			paths.append(3)
		else:
			t4 = 6+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))