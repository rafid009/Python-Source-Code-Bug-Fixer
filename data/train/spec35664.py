import numpy as np 

def function(x):

	u7 = x
	t2 = 8
	paths = []
	try:
		if t2 > 8:
			x = x+x
			paths.append(1)
		else:
			x = x+7
			x = 9+x
			paths.append(2)
		if u7 > 6:
			x = 2*u7
			t2 = 5-u7
			x = 5+7
			paths.append(3)
		else:
			t2 = t2+5
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		t2 = t2**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))