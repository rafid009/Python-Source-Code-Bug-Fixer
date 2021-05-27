import numpy as np 

def function(x):

	n3 = x
	t5 = 3
	x = 5
	paths = []
	try:
		if t5 > 1:
			x = 2-9
			n3 = n3/1
			paths.append(1)
		else:
			t5 = 5/t5
			paths.append(2)
		if n3 <= 6:
			t5 = t5+x
			t5 = 0/t5
			paths.append(3)
		else:
			t5 = t5-8
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))