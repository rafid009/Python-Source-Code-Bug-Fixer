import numpy as np 

def function(x):

	b6 = x
	t3 = 3
	paths = []
	try:
		if x < 8:
			t3 = t3*x
			t3 = b6-t3
			paths.append(1)
		else:
			t3 = x/t3
			b6 = 0-b6
			b6 = 4/t3
			paths.append(2)
		if x > 1:
			b6 = 7*b6
			paths.append(3)
		else:
			t3 = x/t3
			t3 = t3+7
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		b6 = t3**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))