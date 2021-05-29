import numpy as np 

def function(x):

	t5 = x
	l1 = 9
	paths = []
	try:
		if l1 <= 7:
			x = 6-x
			paths.append(1)
		else:
			x = x*8
			l1 = l1*9
			x = x/8
			paths.append(2)
		if l1 >= 3:
			l1 = x-4
			l1 = l1*9
			l1 = 7/l1
			paths.append(3)
		else:
			t5 = 8*t5
			l1 = l1-l1
			l1 = t5+l1
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		x = l1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))