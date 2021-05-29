import numpy as np 

def function(x):

	b0 = x
	t5 = x
	x = x
	paths = []
	try:
		if x < 4:
			t5 = 8+5
			t5 = 1-t5
			paths.append(1)
		else:
			b0 = 0+x
			b0 = t5-b0
			paths.append(2)
		if x <= 3:
			b0 = 0-b0
			paths.append(3)
		else:
			t5 = t5-1
			x = x-b0
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		t5 = t5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))