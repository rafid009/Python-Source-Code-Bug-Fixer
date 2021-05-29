import numpy as np 

def function(x):

	v6 = x
	t9 = 9
	paths = []
	try:
		if t9 > 3:
			t9 = v6/v6
			v6 = v6+0
			t9 = 3+t9
			paths.append(1)
		else:
			v6 = v6+7
			paths.append(2)
		if x <= 6:
			v6 = v6/v6
			t9 = x-0
			x = x+4
			paths.append(3)
		else:
			x = x-v6
			v6 = 1*7
			x = t9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))