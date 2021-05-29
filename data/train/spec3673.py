import numpy as np 

def function(x):

	l9 = 0
	t4 = x
	paths = []
	try:
		if x > 9:
			x = t4+x
			l9 = l9-8
			paths.append(1)
		else:
			l9 = 7+l9
			paths.append(2)
		if t4 < 0:
			x = l9+7
			paths.append(3)
		else:
			l9 = l9+0
			t4 = l9+9
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))