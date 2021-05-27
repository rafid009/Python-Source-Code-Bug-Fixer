import numpy as np 

def function(x):

	k1 = x
	t5 = 5
	paths = []
	try:
		if t5 > 3:
			x = 7/x
			t5 = t5+t5
			t5 = 6/t5
			paths.append(1)
		else:
			t5 = 7-2
			t5 = t5-x
			paths.append(2)
		if t5 < 5:
			k1 = k1+8
			paths.append(3)
		else:
			t5 = t5/9
			x = x*t5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))