import numpy as np 

def function(x):

	t6 = x
	l3 = 3
	paths = []
	try:
		if l3 > 4:
			t6 = t6-7
			x = 8*2
			paths.append(1)
		else:
			t6 = 9-3
			l3 = 4-l3
			paths.append(2)
		if l3 <= 5:
			t6 = 5+1
			t6 = t6-0
			x = 0-8
			paths.append(3)
		else:
			t6 = t6+2
			l3 = 2*l3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))