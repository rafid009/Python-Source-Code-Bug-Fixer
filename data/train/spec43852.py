import numpy as np 

def function(x):

	i3 = x
	t1 = x
	paths = []
	try:
		if x < 5:
			x = t1+x
			t1 = 4/i3
			paths.append(1)
		else:
			t1 = t1-8
			i3 = i3-8
			i3 = i3+x
			paths.append(2)
		if x >= 6:
			t1 = 0-8
			paths.append(3)
		else:
			t1 = 0/i3
			i3 = 9+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))