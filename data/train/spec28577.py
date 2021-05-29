import numpy as np 

def function(x):

	t1 = 7
	l4 = x
	paths = []
	try:
		if x <= 9:
			t1 = t1+t1
			x = x/8
			paths.append(1)
		else:
			t1 = t1-1
			t1 = t1-7
			x = x*3
			paths.append(2)
		if l4 <= 2:
			l4 = x*9
			x = x/3
			t1 = 8/l4
			paths.append(3)
		else:
			t1 = t1*t1
			x = 2+4
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		l4 = t1**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))