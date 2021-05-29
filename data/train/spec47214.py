import numpy as np 

def function(x):

	t6 = x
	l1 = 3
	paths = []
	try:
		if x <= 5:
			x = x+5
			paths.append(1)
		else:
			l1 = l1*l1
			paths.append(2)
		if l1 > 7:
			t6 = l1/7
			l1 = 8+7
			x = x*8
			paths.append(3)
		else:
			l1 = l1*8
			l1 = 2-l1
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))