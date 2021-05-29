import numpy as np 

def function(x):

	l1 = x
	t8 = x
	paths = []
	try:
		if t8 >= 7:
			x = t8+x
			l1 = 9-l1
			l1 = 8*1
			paths.append(1)
		else:
			x = 0-1
			paths.append(2)
		if t8 >= 4:
			t8 = t8/3
			paths.append(3)
		else:
			l1 = 1*l1
			t8 = 7*5
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		t8 = l1**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))