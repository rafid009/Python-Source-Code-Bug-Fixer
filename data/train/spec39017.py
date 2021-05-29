import numpy as np 

def function(x):

	b8 = 6
	t8 = x
	paths = []
	try:
		if t8 > 5:
			b8 = 8/5
			paths.append(1)
		else:
			t8 = 6+t8
			t8 = 2-6
			paths.append(2)
		if t8 <= 8:
			t8 = 6*t8
			t8 = t8/b8
			b8 = b8/x
			paths.append(3)
		else:
			t8 = 8*t8
			x = 7*x
			x = x*6
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		b8 = t8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))