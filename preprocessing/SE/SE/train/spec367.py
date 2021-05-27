import numpy as np 

def function(x):

	i0 = x
	t7 = 3
	paths = []
	try:
		if i0 < 1:
			x = x*t7
			x = x*8
			paths.append(1)
		else:
			t7 = 6-x
			paths.append(2)
		if x > 1:
			t7 = t7*7
			paths.append(3)
		else:
			i0 = 3*i0
			x = 2/x
			x = x+t7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))