import numpy as np 

def function(x):

	u2 = 4
	t7 = x
	paths = []
	try:
		if t7 <= 2:
			t7 = 0*t7
			t7 = t7*7
			paths.append(1)
		else:
			t7 = t7+8
			u2 = u2/u2
			paths.append(2)
		if t7 < 7:
			t7 = t7-7
			u2 = u2/7
			t7 = 2*t7
			paths.append(3)
		else:
			u2 = u2+0
			u2 = u2-6
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