import numpy as np 

def function(x):

	t7 = x
	l0 = 1
	paths = []
	try:
		if x >= 4:
			t7 = 9-l0
			l0 = x*9
			paths.append(1)
		else:
			t7 = t7/l0
			paths.append(2)
		if l0 >= 4:
			l0 = x/l0
			x = 2*2
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))