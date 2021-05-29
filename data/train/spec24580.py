import numpy as np 

def function(x):

	t7 = x
	b8 = 4
	paths = []
	try:
		if b8 <= 5:
			b8 = 7*b8
			paths.append(1)
		else:
			b8 = t7+8
			x = 0*2
			b8 = 7*b8
			paths.append(2)
		if b8 > 0:
			x = x-2
			x = x+6
			b8 = b8*4
			paths.append(3)
		else:
			b8 = b8*7
			t7 = 8/6
			x = 4*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))