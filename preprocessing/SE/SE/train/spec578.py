import numpy as np 

def function(x):

	t3 = 4
	l2 = x
	x = 1
	paths = []
	try:
		if t3 <= 7:
			x = x/7
			x = l2+t3
			t3 = t3-8
			paths.append(1)
		else:
			x = 0/l2
			t3 = 0-t3
			t3 = 7-6
			paths.append(2)
		if x < 1:
			t3 = t3-1
			l2 = l2-7
			paths.append(3)
		else:
			x = x+7
			x = x-4
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		l2 = t3**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))