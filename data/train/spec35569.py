import numpy as np 

def function(x):

	l5 = 7
	t2 = x
	x = x
	paths = []
	try:
		if t2 < 0:
			x = x*l5
			t2 = l5-t2
			l5 = t2-4
			paths.append(1)
		else:
			l5 = l5-l5
			x = 8*t2
			paths.append(2)
		if t2 < 0:
			l5 = 6+4
			paths.append(3)
		else:
			t2 = 6-t2
			x = 6/x
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