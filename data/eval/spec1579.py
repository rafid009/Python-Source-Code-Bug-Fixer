import numpy as np 

def function(x):

	l7 = 9
	t3 = 7
	paths = []
	try:
		if t3 < 3:
			x = 4+x
			t3 = t3-l7
			paths.append(1)
		else:
			x = x/2
			l7 = l7+2
			x = 3/4
			paths.append(2)
		if t3 <= 8:
			t3 = 4-t3
			paths.append(3)
		else:
			t3 = t3-4
			l7 = l7-1
			l7 = 3*7
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t3 = t3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))