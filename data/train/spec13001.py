import numpy as np 

def function(x):

	t5 = 5
	b3 = x
	x = x
	paths = []
	try:
		if t5 >= 3:
			t5 = t5-9
			paths.append(1)
		else:
			t5 = t5*b3
			paths.append(2)
		if b3 > 2:
			t5 = t5+b3
			paths.append(3)
		else:
			b3 = b3-8
			t5 = t5-2
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