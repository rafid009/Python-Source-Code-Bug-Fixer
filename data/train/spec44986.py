import numpy as np 

def function(x):

	t1 = x
	l7 = 3
	paths = []
	try:
		if l7 < 9:
			x = x-x
			t1 = 6-t1
			paths.append(1)
		else:
			l7 = x-4
			x = t1+l7
			l7 = 2*3
			paths.append(2)
		if x <= 2:
			l7 = l7*l7
			l7 = l7*2
			paths.append(3)
		else:
			t1 = 2+t1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))