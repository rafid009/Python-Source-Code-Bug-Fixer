import numpy as np 

def function(x):

	b5 = 0
	t5 = 6
	paths = []
	try:
		if x < 7:
			t5 = 6/t5
			b5 = b5+5
			x = x/8
			paths.append(1)
		else:
			x = x*4
			t5 = t5*t5
			x = 6/x
			paths.append(2)
		if t5 >= 1:
			b5 = b5-1
			b5 = x/b5
			x = x-5
			paths.append(3)
		else:
			b5 = t5*b5
			b5 = b5/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))