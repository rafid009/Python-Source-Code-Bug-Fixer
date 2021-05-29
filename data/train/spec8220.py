import numpy as np 

def function(x):

	t3 = x
	b8 = x
	paths = []
	try:
		if t3 <= 0:
			b8 = b8+b8
			t3 = t3-7
			paths.append(1)
		else:
			t3 = 2+6
			x = 1+x
			paths.append(2)
		if x <= 3:
			x = 3+x
			t3 = t3*x
			paths.append(3)
		else:
			t3 = t3+t3
			b8 = b8+x
			b8 = b8/9
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		b8 = t3**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))