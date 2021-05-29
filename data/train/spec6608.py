import numpy as np 

def function(x):

	t5 = x
	b6 = x
	paths = []
	try:
		if x < 6:
			b6 = b6*8
			paths.append(1)
		else:
			t5 = 5*t5
			t5 = x-t5
			t5 = t5*1
			paths.append(2)
		if b6 < 2:
			b6 = 2*t5
			b6 = x+b6
			paths.append(3)
		else:
			t5 = t5+4
			b6 = 7/4
			t5 = t5-9
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))